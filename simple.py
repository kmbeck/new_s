# # # # #
# Kyle Beck
# ---------
# Takes a word count and makes a cool matrix effect.
# # # # #

import random
import shutil
import time

LOOP_DELAY=0.01
LINE_WIDTH=shutil.get_terminal_size()[0]
LINE_HEIGHT=shutil.get_terminal_size()[0]

def play_simple_effect(data):
    weighted_list = _gen_weighted_list(data)
    cur_line = ''
    cur_word = ''
    while True:
        time.sleep(LOOP_DELAY)
        if len(cur_line) >= LINE_WIDTH:
            print('')
            cur_line = ''
        if len(cur_word) == 0:
            cur_word = _get_random_word(weighted_list)
            cur_line += ' '
        else:
            cur_line += cur_word[0]
            cur_word = cur_word[1:]	
        print(cur_line, end='\r')

def _gen_weighted_list(data):
    '''
    Takes word count dict and expands it into a weighted list we can use
    for random selection. Returns list.
    '''
    retval = []
    for key,val in data.items():
    	for i in range(0, val):
            retval.append(key)
    return retval

def _get_random_word(_list):
    '''
    Return a random element from the list.
    '''
    return _list[random.randint(0,len(_list)-1)]
