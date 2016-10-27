```
usage: Formats text as a url of the specified minimum length, with the specified features, made of words drawn from a text file. Default is text of the star spangled banner.
       [-h] [-d DOMAIN_LEN] [-p PREFIX] [-w WORDS] url_len parts_params_len

positional arguments:
  url_len               minimum length of url in characters
  parts_params_len      parts_len:params_len - len is in words, if both are
                        included and the resulting url is not over url_len,
                        more params will be added

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN_LEN, --domain_len DOMAIN_LEN
                        length of the 'domain' part of the url in words.
                        defaults to 5
  -p PREFIX, --prefix PREFIX
                        defaults to http://
  -w WORDS, --words WORDS
                        name of a text file to get words from
```
