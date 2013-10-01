from copy import *
from battleship_data import Board


class Grid(object):
    ''' A visual representation of a Battleship game board.'''

    def __init__(self, n, board):
        '''(Grid, int) -> NoneType
        A new Grid object.
        '''

        self._size = n
        self._grid = self.generate_grid()
        self._board = board

    def generate_grid(self):
        '''(Grid) -> dict'''

        grid_dict = {}
        # A blank space (water) in the grid will be denoted by ~
        space = '~'.center(len(str(self._size)))
        space_list = []
        for i in range(0, self._size):
            space_list += [space]
        for i in range(0, self._size):
            # copy creates a shallow copy of space_list; without this,
            # each key in grid_dict would be assigned the same list at the
            # same memory location as values.
            grid_dict[i] = copy(space_list)

        return grid_dict

    def add_ships_to_grid(self):
        '''(Grid) -> NoneType'''

        # add_ships_to_grid is separate from update_grid because ships only
        # have to be added once (after the initial ship selection/addition
        # stage in the beginning of the game), whereas hits and misses have to
        # be updated every turn.
        for L in self._board.board_data()[0]:
            self._grid[L[0]][L[1]] = 'O'.center(len(str(self._size)))

    def update_grid(self):
        '''(Grid) -> NoneType'''

        # Hits
        for L in self._board.board_data()[1]:
            self._grid[L[0]][L[1]] = 'X'.center(len(str(self._size)))
        # Misses
        for L in self._board.board_data()[2]:
            self._grid[L[0]][L[1]] = 'm'.center(len(str(self._size)))

    def show_grid(self):
        '''(Grid) -> str'''

        space = ' '.center(len(str(self._size)))
        print space,
        for n in range(0, self._size - 1):
            print space + str(n).center(len(str(self._size))),
        print space + str(self._size - 1)

        for n in range(0, self._size):
            print str(n).center(len(str(self._size))), self.show_row(n)

    def show_row(self, n):
        '''(Grid, int) -> list)'''

        x = ''
        space = ' '.center(len(str(self._size)))
        for square in self._grid[n]:
            x += space + square + ' '
        return x

    def show_guess_grid(self):
        '''(Grid) -> str
        Return a copy of the game grid, showing only hits and misses (no unhit
        ships.'''

        grid = deepcopy(self._grid)
        for row in grid.keys():
            for index in range(len(grid[row])):
                # Replace unhit ships with water
                if grid[row][index].find('O') != -1:
                    grid[row][index] = '~'.center(len(str(self._size)))

        space = ' '.center(len(str(self._size)))
        print space,
        for n in range(0, self._size - 1):
            print space + str(n).center(len(str(self._size))),
        print space + str(self._size - 1)

        for n in range(0, self._size):
            print str(n).center(len(str(self._size))), \
                  self.show_given_row(grid[n])

    def show_given_row(self, row):
        '''(Grid, list) -> str'''

        x = ''
        space = ' '.center(len(str(self._size)))
        for square in row:
            x += space + square + ' '
        return x
