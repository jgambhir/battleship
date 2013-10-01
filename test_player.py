import unittest
from battleship_data import Board
from player import User


class TestUser(unittest.TestCase):

    def setUp(self):
        '''Set up a new empty User object, with an empty board of size 10.'''

        board = Board(10)
        self.user = User(10, board)

    def test_AI_guess_registered(self):
        '''Make sure a random AI guess gets added to the list of guesses.'''

        coordinate = self.user.AI_guess()
        self.assertTrue(coordinate in self.user._guesses, \
                        'AI guess was not added to list of guesses.')

    def test_invalid_guess_big_numbers(self):
        '''Make sure a guess with a coordinate equal to the board size is
        considered invalid.
        '''

        # [10, 1] is invalid because the board is numbered from zero, so
        # a board of size 10 only goes up to 9.
        self.assertTrue(self.user.invalid_guess([10, 1]), \
                        'An invalid row coordinate was declared valid.')

    def test_invalid_guess_already_guessed(self):
        '''Make sure a coordinate that has already been guessed is invalid.'''

        self.user._guesses.append([0, 0])
        self.assertTrue(self.user.invalid_guess([0, 0]), \
                        'A guess made twice was declared valid.')


if __name__ == '__main__':
    unittest.main()
