from battleship_data import Board
import random
import os


class User(object):
    ''' A Battleship game player.'''

    def __init__(self, n, board):
        '''(User, Board) -> NoneType
        A new User.
        '''
        self._guesses = []
        self._size = n
        self._board = board

    def AI_guess(self):
        '''(User) -> List'''

        guess_row = random.randint(0, self._size - 1)
        guess_col = random.randint(0, self._size - 1)
        coordinate = [guess_row, guess_col]
        while self.invalid_guess(coordinate):
            guess_row = random.randint(0, self._size - 1)
            guess_col = random.randint(0, self._size - 1)
            coordinate = [guess_row, guess_col]
        self._guesses += [coordinate]
        return coordinate

    def invalid_guess(self, coordinate):
        '''(User, list) -> Bool'''

        return (coordinate in self._guesses or len(coordinate) > 2 or  \
           coordinate[0] > (self._size - 1) or coordinate[1] > \
           (self._size - 1))

    def human_turn(self):
        '''(User) -> list'''
        guess = raw_input('Enter in the coordinates (in format (row,column) '\
                          + '[example: (0,1)]) you want to \nhit on your '\
                          + 'opponent\'s grid: ')
        try:
            # Turn the user-inputted coordinates from a string to a list
            guess = guess.strip()[1: -1].split(',')
            guess = [int(guess[0]), int(guess[1])]
            while self.invalid_guess(guess):
                print 'Invalid guess.'
                guess = raw_input('Enter in the coordinates (in format (row,'\
                                  + 'column) [example: (0,1)]) you want to \n'\
                                  + 'hit on your opponent\'s grid: ')
                guess = guess.strip()[1:-1].split(',')
                guess = [int(guess[0]), int(guess[1])]
            self._guesses.append(guess)
            return guess
        except:
            print 'Invalid guess format!'
            return self.human_turn()


def clear():
    '''() -> NoneType
    Clear the output window (only works in console).
    '''

    # Code via popcnt on stackoverflow.com
    os.system(['clear', 'cls'][os.name == 'nt'])
