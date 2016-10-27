import re
import argparse

just_letters = re.compile('[^a-zA-Z]')

def get_words(filename="star_spangled_banner.txt"):
    with open(filename, 'r') as f:
        words = ' '.join(f.readlines()).replace('-', ' ').split()
    words = [just_letters.sub('', word.lower()) for word in words]
    return words

def words_for_length(words, length, prefix = 'http://'):
    current_len = len(prefix)
    chosen_words = []
    iterator = iter(words)
    while current_len < length:
        try:
            chosen_words.append(iterator.next())
            current_len += len(chosen_words[-1]) + 1
        except:
            print "bloop"
            break
    return chosen_words

def make_url(url_len, domain_len = 5, parts_params_len = None, words = None, prefix = 'http://'):
    parts_len, params_len = [int(x) if x != '' else None for x in parts_params_len.split(":")]
    if words == None:
        words = get_words()
    else:
        words = get_words(words)
    use_words = words_for_length(words, url_len, prefix)
    if parts_len != None and params_len != None:
        # both are included, see if generated url is long enough
        try:
            num_words = domain_len + parts_len + params_len
            prospective_length = len(prefix) + sum([len(word) + 1 for word in words[:num_words]])
            if prospective_length >= url_len:
                use_words = words[:num_words]
        except:
            pass
    domain_idx = domain_len if len(use_words) >= domain_len else 0
    if parts_len == None and params_len == None:
        idx = (len(use_words) - domain_idx)/2
    elif parts_len == None:
        idx = max(domain_idx, len(use_words) - params_len)
    else:
        idx = min(parts_len + domain_idx, len(use_words))
    domain = use_words[:domain_idx]
    parts = use_words[domain_idx:idx]
    params = use_words[idx:]
    params.append(params[-1]) # to make a guaranteed even number
    param_pairs = zip(*[iter(params)] * 2)
    url = prefix + ".".join(domain) + "/" + "/".join(parts) + "?" + "&".join(["%s=%s" % (a, b) for a, b in param_pairs])
    return url


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Formats text as a url of the specified minimum length, with the specified features, made of words drawn from a text file. Default is text of the star spangled banner.")
    parser.add_argument("url_len", type=int, help="minimum length of url in characters")
    parser.add_argument("parts_params_len", help="parts_len:params_len - len is in words, if both are included and the resulting url is not over url_len, more params will be added")
    parser.add_argument("-d", "--domain_len", type=int, default=5, help="length of the 'domain' part of the url in words. defaults to %(default)s")
    parser.add_argument("-p", "--prefix", default="http://", help="defaults to %(default)s")
    parser.add_argument("-w", "--words", help="name of a text file to get words from")
    url = make_url(**vars(parser.parse_args()))
    print url
    print "actual length:", len(url)
