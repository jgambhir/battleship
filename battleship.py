from battleship_data import *
from player import *
from grid import *
import random
import time


def player_2_type():
    '''() -> str
    Ask the user whether the second player of the game will be a human or
    the computer.
    '''

    player_2 = raw_input('Type human or computer and press enter: ')
    player_2 = player_2.lower().strip()
    if player_2 == 'human' or player_2 == 'computer':
        return player_2
    else:
        print 'invalid player type!'
        return player_2_type()


def board_size():
    '''() -> int
    Ask the user for their desired Battleship board size.
    '''

    size = raw_input('Enter in your desired board size (greater than 1): ')
    try:
        size = int(size)
        if size <= 1:
            print 'Board size too small.'
            return board_size()
    except:
        print 'invalid board size!'
        return board_size()
    return size


def place_ships(board, board_2):
    '''(Board, Board) -> str
    Randomly place a ship of user-specified size (between 2 and 5) on both
    players' boards, not overlapping with any other ships.
    '''

    ship_size = raw_input('Enter the desired ship size (2-5) or type ' + \
                          '\'done\' to finish adding ships: ')
    ship_size = ship_size.strip().lower()
    if ship_size == 'done':
        return 'All ships have been added. Now on to the game!\n'
    else:
        try:
            ship_size = int(ship_size)
            if ship_size < 2 or ship_size > 5:
                return 'Ship size must be between 2 and 5!\n'
            else:
                # direction 0 means a horizontal ship, 1 is vertical
                direction = random.randint(0, 1)
                # Randomly generate a valid ship position and add to player 1's
                # board
                start_pos = board.generate_start_pos(ship_size, direction)
                tries = 0
                # 20 tries will be made to randomly add a ship of ship_size to
                # the board; random placement limits the number of ships that
                # can be added to the board.
                while not board.valid_ship(start_pos, ship_size, direction) \
                      and tries < 20:
                    direction = random.randint(0, 1)
                    start_pos = board.generate_start_pos(ship_size, direction)
                    tries += 1
                if tries == 20:
                    return 'Ship could not be added. Stop adding ships or ' \
                           + 'choose a smaller size.\n'
                else:
                    board.add_ship(start_pos, ship_size, direction)

                # Randomly place a ship of the same size to player 2's board
                direction_2 = random.randint(0, 1)
                start_pos_2 = board_2.generate_start_pos(ship_size, \
                                                         direction_2)
                tries = 0
                while not board_2.valid_ship(start_pos_2, ship_size, \
                                             direction_2) and tries < 20:
                    direction_2 = random.randint(0, 1)
                    start_pos_2 = board_2.generate_start_pos(ship_size, \
                                                             direction_2)
                    tries += 1
                if tries == 20:
                    return 'Ship could not be added. Stop adding ships or ' \
                           + 'choose a smaller size.'
                else:
                    board_2.add_ship(start_pos_2, ship_size, direction_2)
                    return 'Ship added!'
        except:
            return 'Invalid ship size!'


if __name__ == '__main__':
    print 'Welcome to Battleship! This is a two player game, so grab another '\
          + '\nperson, or you can play against the computer.\n'
    print 'Will player 2 be a human or the computer?'
    p2_type = player_2_type()
    print '\nBattleship is played on an square nxn board. How big do you want'\
          + '\nyour board to be?'
    size = board_size()

    p1_board = Board(size)
    p2_board = Board(size)
    player_1 = User(size, p1_board)
    player_2 = User(size, p2_board)
    p1_grid = Grid(size, p1_board)
    p2_grid = Grid(size, p2_board)

    print '\nNow ships have to be added to the board. Ships will be placed' + \
    '\nrandomly for both players.\n'
    ship_status = place_ships(p1_board, p2_board)
    while ship_status == 'All ships have been added. Now on to the game!\n':
        print 'At least one ship has to be added.'
        ship_status = place_ships(p1_board, p2_board)
    print ship_status
    while ship_status != 'All ships have been added. Now on to the game!\n':
        ship_status = place_ships(p1_board, p2_board)
        print ship_status

    p1_grid.add_ships_to_grid()
    p2_grid.add_ships_to_grid()

    raw_input('Press enter to continue and start the game!')
    clear()
    t0 = time.time()
    turns = 0

    coordinate = False
    while not p1_board.game_over() and not p2_board.game_over():
        turns += 1
        print 'Player 1\'s turn.'
        time.sleep(3)
        clear()
        print 'Player 1, here is your grid.'
        print 'O is a ship, ~ is water, X is a hit, m is a miss.'
        if coordinate:
            print 'Last turn, Player 2 guessed %s. That\'s a %s' \
                  % (coordinate, hit_or_miss)
        p1_grid.update_grid()
        p1_grid.show_grid()
        p2_grid.update_grid()
        print 'Here are your hits and misses on your opponent\'s grid.'
        p2_grid.show_guess_grid()
        coordinate = player_1.human_turn()
        hit_or_miss = p2_board.register_guess(coordinate)
        print 'That\'s a %s' % (hit_or_miss)
        time.sleep(3)
        if p2_board.game_over():
            break
        clear()

        if p2_type == 'human':
            print 'Player 2\'s turn.'
            time.sleep(3)
            clear()
            print 'Player 2, here is your grid.'
            print 'O is a ship, ~ is water, X is a hit, m is a miss.'
            print 'Last turn, Player 1 guessed %s. That\'s a %s' \
                  % (coordinate, hit_or_miss)
            p2_grid.update_grid()
            p2_grid.show_grid()
            p1_grid.update_grid()
            print 'Here are your hits and misses on your opponent\'s grid.'
            p1_grid.show_guess_grid()
            coordinate = player_2.human_turn()
            hit_or_miss = p1_board.register_guess(coordinate)
            print 'That\'s a %s' % (hit_or_miss)
            time.sleep(3)
            clear()
        # Player 2 is the computer
        else:
            print 'Player 2\'s turn.'
            coordinate = player_2.AI_guess()
            hit_or_miss = p1_board.register_guess(coordinate)
            print 'Computer player 2 guesses %s. That\'s a %s.' \
                  % (coordinate, hit_or_miss)
            time.sleep(3)

    t1 = time.time()
    print 'The game is over.'
    if p1_board.game_over():
        print 'Player 2 won in %s turns, with a time of %s seconds.' \
              % (turns, int(t1 - t0))
    else:
        print 'Player 1 won in %s turns, with a time of %s seconds.' \
              % (turns, int(t1 - t0))
