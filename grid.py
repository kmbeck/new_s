# # # # #
# Kyle Beck
# ---------
# Matrix 'Grid' object.
# # # # #

import random
import shutil
import time

class Grid:
    '''
    GRID DISPLAYED ON TERMINAL:

    [2] b b b b b b b b b b
    [1] u u u u u u u u u u
    [0] f f f f f f f f f f        
       #####################
    [0]#c c c c c c c c c c#
    [1]#o o o o o o o o o o#
    [2]#l l l l l l l l l l#
    [3]#                   #
    [4]#1 2 3 4 5 6 7 8 9 0#
    [5]#                   #
       #####################
    '''
    def __init__(self, count_data=None):
        self.count_data = count_data

        # Settings for effect
        self.loop_delay = 0.15
        self.density_factor = 0.5
       
       # [width,height]
        self.dimensions = []
        self._refresh_dimensions()

        self.cols = []      # Columns displayed in terminal
        self.col_bufs = []  # str buffer 'above' terminal

        self._gen_cols()
        self._pop_col_bufs()
        #self._drop_down()

    def begin_animation(self):
        '''Call this to updated the grid animation in a loop...'''
        self._drop_down()
        while True:
            time.sleep(self.loop_delay)
            self.update()

    def update(self):
        '''Call this to update the grid animation...'''
        prev_dimensions = self.dimensions
        self._refresh_dimensions()
        if self.dimensions != prev_dimensions:
            # Reinitialize entire display when terminal size changes.
            self._gen_cols()
            self._drop_down()
        self._pop_col_bufs()
        self._drip_down()
        
        # Print to terminal
        for i in range(0, len(self.cols[0])):
            new_line = ''
            for j in range(0, len(self.cols)):
                # Only display text in every other colum.
                # print ith character of jth column.
                if j%2 == 0:
                    new_line += self.cols[j][i]
                else:
                    new_line += ' '
            print(new_line)

    def set_count_data(data):
        '''Set data this grid will use to generate data.'''
        self.count_data = data

    def _drip_down(self):
        '''Step a row of characters from the col_bufs to the cols.'''
        for i in range(0, len(self.cols)):
            self.cols[i] = self.col_bufs[i][0] + str(self.cols[i][:-1])
            self.col_bufs[i] = self.col_bufs[i][1:]

    def _drop_down(self):
        '''Hacky fast forward drip down...'''
        for i in range(0, self.dimensions[1] * 5):
            self._pop_col_bufs()
            self._drip_down()

    def _refresh_dimensions(self):
        '''Set dimensions to current size of terminal window.'''
        self.dimensions = shutil.get_terminal_size()

    def _gen_cols(self):
        '''Initialize columns and column buffers for the grid.'''
        self.cols.clear()
        self.col_bufs.clear()
        self.col_bufs = [[] for i in range(0, self.dimensions[0]-1)]
        for i in range(0, self.dimensions[0]-1):
            self.cols.append([' ' for i in range(0, self.dimensions[1]-1)])


    def _pop_col_bufs(self):
        '''If a column buffer is empty, fill it with random words.'''
        for c in self.col_bufs:
            if len(c) == 0:
                while len(c) < self.dimensions[1]:
                    density = (self.dimensions[1] / self.density_factor) - 1
                    pad = ''.join([' ' for i in range(0, random.randint(3, density))])
                    word = self._get_random_word()[::-1]
                    if len(c) + len(word) + len(pad) < self.dimensions[0] * 2:
                        c += word + pad
                    else:
                        break

    def _get_random_word(self):
        '''Return random element from self.count_data.'''
        return self.count_data[random.randint(0, len(self.count_data)-1)]
