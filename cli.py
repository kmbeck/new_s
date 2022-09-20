# # # # # 
# Kyle Beck
# ---------
# CLI functionality for running the program.
# # # # #

import calc
import directories as dirs
import getopt
import grid
import simple
import scrape
import sys

def main(argv):

    help_msg = _gen_help_msg() 

    params = {      # Params & default values.
        'url_file':'res/urls/feed_urls.txt',
    }
    
    try:
        opts,args = getopt.getopt(
            argv,
            'h?',
            [
                'help',
                'url_file=',
                'uf='
            ]
        )
    except getopt.GetoptError as e:
        trace = traceback.format_exc()
        print(trace)
        return

    for opt,val in opts:
        if opt in ['--help','-h','-?']:
            print(help_msg)
            return
        elif opt in ['--url_file','--uf']:
            params['url_file'] = val

    print('Beginning execution from command line.')
    #print(str(params))
    data = scrape.compile_feed_data(params['url_file'])
    data = calc.clean_data(data)
    word_count = calc.calc_word_count(data)
    weighted_list = calc.gen_weighted_list(word_count) 
    matrix_effect = grid.Grid(weighted_list)
    matrix_effect.begin_animation()
            

def _gen_help_msg():
    '''Displays cli help message in terminal.'''
    retval = ''
    with open(dirs.get('file_cli_help'), 'r', encoding='utf-8') as f:
        retval = f.read()
    return retval

# # # # # #
# Hook to execute main function from command line.
if __name__ == '__main__':
    main(sys.argv[1:])
