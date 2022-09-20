# # # # #i
# Kyle Beck
# ---------
# Runs statistical tests over data gathered from feeds.
# # # # #

import directories as dirs
import re

def clean_data(data):
    '''Takes a list of strings and gets them ready for testing.'''

    word_filter_list = open(dirs.get('file_word_filter'),'r',encoding='utf-8').read().split('\n')
    word_filter_list = [w.upper() for w in word_filter_list]
    # Convert to lower case & remove blanks.
    data = [d.upper() for d in data if d not in ['',None]]
    for i in range(0, len(data)):
        data[i] = data[i].split(' ')
        # Strip out 1 length words.
        data[i] = [d for d in data[i] if len(d) > 1]
        # Filter out unwanted words.
        data[i] = [d for d in data[i] if d not in word_filter_list]
        # Strip out punctuation.
        data[i] = [re.sub(r'[^\w\s]','',d) for d in data[i]]
    return data    

def calc_word_count(data):
    '''Takes cleaned data and performs a simple word count. Returns dict{"word":0}'''
    count_dict = {}
    for d in data:
        for w in d:
            if w not in count_dict:
                count_dict[w] = 1
            else:
                count_dict[w] += 1
    count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1]))
    #print(str(count_dict))
    return count_dict

def gen_weighted_list(data):
    '''
    Takes word count dict and expands it into a weighted list we can use
    for random selection. Returns list.
    '''
    retval = []
    for key,val in data.items():
        for i in range(0, val):
            retval.append(key)
    return retval
    
        
