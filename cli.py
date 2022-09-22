# # # # # 
# Kyle Beck
# ---------
# CLI functionality for running the program.
# # # # #

import calc
import directories as dirs
import getopt
import grid
import scrape
import sys
import traceback

def main(argv):

    help_msg = _gen_help_msg() 

    params = {      # Params & default values.
        'url_file':'res/urls/feed_urls.txt',
        'scroll_speed':0.15,
        'density':0.5
    }
    
    try:
        opts,args = getopt.getopt(
            argv,
            'h?f:',
            [
                'help',
                'url_file=',
                'scroll_speed=',
                'density='
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
        elif opt in ['--url_file','-f']:
            params['url_file'] = val
        elif opt == '--scroll_speed':
            params['scroll_speed'] = float(val)
        elif opt == '--density':
            params['density'] = float(val)

    print('Beginning execution from command line.')
    data = scrape.compile_feed_data(params['url_file'])
    data = calc.clean_data(data)
    word_count = calc.calc_word_count(data)
    weighted_list = calc.gen_weighted_list(word_count) 
    matrix_effect = grid.Grid(weighted_list)
    matrix_effect.loop_delay = params['scroll_speed']
    matrix_effect.density_factor = params['density']
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
