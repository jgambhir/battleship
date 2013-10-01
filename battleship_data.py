import random
from copy import copy


class Board(object):
    ''' The data of a Battleship game board.'''

    def __init__(self, n):
        ''' (Board) -> NoneType
        A new empty board of size n.
        '''
        self._board_size = n
        self._ships = []
        self._hits = []
        self._misses = []

    def generate_start_pos(self, ship_size, direction):
        ''' (Board, int, int) -> list
        Randomly generate and return a starting position for a ship of size
        ship_size.
        '''

        # Ship orientation is horizontal
        if direction == 0:
            start_row = random.randint(0, self._board_size - 1)
            # The farthest valid starting position for a ship of size n
            # is n - 1 squares away from the last square
            start_col = random.randint(0, self._board_size - ship_size)
        # Ship orientation is vertical
        else:
            start_col = random.randint(0, self._board_size - 1)
            start_row = random.randint(0, self._board_size - ship_size)
        return [start_row, start_col]

    def valid_ship(self, start_pos, ship_size, direction):
        ''' (Board, list, int, str) -> Bool
        Check whether a ship (based on a starting position, size, and
        direction) overlaps with any other ships.
        '''

        n = 0
        coordinate = start_pos
        while n < ship_size:
            if coordinate in self._ships:
                return False
            else:
                # Create a shallow copy of coordinate; not doing changes
                # start_pos, which leads to errors and incorrect values
                # wherever start_pos is used.
                coordinate = copy(coordinate)
                if direction == 0:
                    coordinate[1] += 1
                else:
                    coordinate[0] += 1
                n += 1
        return True

    def add_ship(self, start_pos, ship_size, direction):
        ''' (Board, list, int, str) -> str
        Add a valid ship to the board.
        '''

        n = 1
        coordinate = start_pos
        self._ships += [coordinate]
        while n < ship_size:
            # See comment starting on line 37 regarding implications of
            # the mutability of coordinate and start_pos
            coordinate = copy(coordinate)
            if direction == 0:
                coordinate[1] += 1
            else:
                coordinate[0] += 1
            self._ships.append(coordinate)
            n += 1

    def register_guess(self, coordinate):
        ''' (Board, list) -> str
        Record and return whether a coordinate has hit a ship, or missed it.
        '''

        if coordinate in self._ships:
            self._hits += [coordinate]
            return 'hit!'
        else:
            self._misses += [coordinate]
            return 'miss!'

    def game_over(self):
        ''' (Board) -> bool
        Return whether the game is over (when all ships have been hit).
        '''

        self._ships.sort()
        self._hits.sort()
        return self._ships == self._hits

    def board_data(self):
        ''' (Board) -> list
        Return a list containing all ships, hits, and misses on the board.
        '''

        return [self._ships, self._hits, self._misses]
