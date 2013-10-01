import unittest
from battleship_data import *


class TestBoard(unittest.TestCase):

    def setUp(self):
        '''Set up a new empty Board object, of board size 10.'''

        self.board = Board(10)

    def test_valid_ship_one(self):
        '''Make sure one valid ship is declared as valid'''

        self.assertTrue(self.board.valid_ship([3, 1], 3, 0), \
                        'Valid ship was declared invalid.')

    def test_add_ship_one(self):
        '''Make sure a ship is recorded correctly in the Board's ship list.'''

        self.board.add_ship([0, 0], 2, 0)
        self.assertEqual(self.board.board_data()[0], [[0, 0], [0, 1]], \
                         'All ship coordinates were not recorded correctly.')

    def test_register_guess_hit(self):
        '''Make sure a hit is registered as a hit.'''

        self.board.add_ship([0, 0], 2, 0)
        self.board.register_guess([0, 0])
        self.assertEqual(self.board.board_data()[1], [[0, 0]], \
                    'Hit coordinate did not show up in hit list')

    def test_register_guess_miss(self):
        '''Make sure a miss is registered as a miss.'''

        self.board.add_ship([0, 0], 2, 0)
        self.board.register_guess([1, 1])
        self.assertEqual(self.board.board_data()[2], [[1, 1]], \
                    'Missed coordinate did not show up in misses list')

    def test_game_over(self):
        '''Make sure the game is declared over when all ships have been hit.'''

        self.board.add_ship([0, 0], 2, 0)
        self.board.register_guess([0, 0])
        self.board.register_guess([0, 1])
        self.assertTrue(self.board.game_over(), \
                        'Game was not declared over when all ships were sunk.')


if __name__ == '__main__':
    unittest.main()
