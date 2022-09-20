# # # # #
# Kyle Beck
# ---------
# Functionality for reading data from feeds.
# # # # #

import feedparser as fp

def compile_feed_data(url_fp):
    '''
    Compiles data returned from all desired feeds. Includes fields 
    specified by user...
    '''
    url_file = open(url_fp, 'r', encoding='utf-8')
    urls = url_file.read().split('\n')
    data = get_feed_data(urls)
    retval = []
    for d in data:
        for e in d.entries:
            retval.append(e.title)
    return retval

def get_feed_data(url):
    '''
    Attempts to retrieve data from the specified url. url can be string 
    or [string].
    '''
    if isinstance(url, str):
        return fp.parse(url)
    elif isinstance(url, list):
        retval = []
        print("Attempting to scrape specified URLS:")
        cnt = 0
        for u in url:
            cnt += 1
            print("                                   ", end="\r")
            end_char="\n"
            if (cnt < len(url)):
                end_char="\r"
            print(f"  ({cnt}/{len(url)})", end=end_char) 
            retval.append(fp.parse(u))
        return retval
