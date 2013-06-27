import unittest

# from Project.ReversiBoard import *


class TestReversiBoard(unittest.TestCase):

    def test_board_size(self):
        board = ReversiBoard()
        self.assertEqual(board.BOARD_SIZE, 8)

    def test_invalid_value_exception_raises(self):
        invalid_value = ReversiBoard()
        with self.assertRaises(InvalidValue):
            invalid_value[2][3] = "F"

    def test_invalid_key_exception_raises(self):
        invalid_key = ReversiBoard()
        with self.assertRaises(InvalidKey):
            invalid_key[2][10] = ReversiBoard.BLACK

    def test_invalid_move_exception_raises(self):
        invalid_move = ReversiBoard()
        with self.assertRaises(InvalidMove):
            invalid_move[0][0] = ReversiBoard.BLACK
            invalid_move[0][0] = ReversiBoard.WHITE

    def test_not_your_turn_exception_raises(self):
        not_your_turn = ReversiBoard()
        with self.assertRaises(NotYourTurn):
            not_your_turn[2][3] = ReversiBoard.BLACK
            not_your_turn[2][2] = ReversiBoard.BLACK

    def test_possible_moves(self):
        board = ReversiBoard()
        possible_moves = board.get_possible_moves(ReversiBoard.BLACK)
        self.assertEqual(possible_moves, [(2, 3), (3, 2), (4, 5), (5, 4)])

    def test_possible_moves_advanced(self):
        board = ReversiBoard()

        board._board = [[ReversiBoard.WHITE
                         for y in range(0, ReversiBoard.BOARD_SIZE)]
                        for x in range(0, ReversiBoard.BOARD_SIZE)]
        board._board[7][7] = ReversiBoard.EMPTY
        board._board[7][5] = ReversiBoard.BLACK

        board.status = ReversiBoard.GAME_IN_PROGRESS
        board._last_move = ReversiBoard.WHITE

        possible_moves = board.get_possible_moves(ReversiBoard.BLACK)
        self.assertEqual(possible_moves, [(7, 7)])

    def test_get_opposites(self):
        board = ReversiBoard()
        self.assertEqual(board.get_cells_to_flip(2, 3, ReversiBoard.BLACK),
                         [(3, 3)])

    def test_get_no_opposites(self):
        board = ReversiBoard()
        self.assertEqual(board.get_cells_to_flip(1, 1, ReversiBoard.BLACK),
                         [])

    def test_invalid_move_exception_raises_move_not_possible(self):
        move_not_possible = ReversiBoard()
        with self.assertRaises(InvalidMove):
            move_not_possible[1][1] = ReversiBoard.BLACK

    def test_basic_game_update(self):
        board = ReversiBoard()
        board[2][3] = ReversiBoard.BLACK
        self.assertEqual(board.get_possible_moves(ReversiBoard.WHITE),
                         [(2, 2), (2, 4), (4, 2)])

    def test_advanced_game_update(self):
        board = ReversiBoard()
        board[2][3] = ReversiBoard.BLACK
        board[4][2] = ReversiBoard.WHITE
        board[5][3] = ReversiBoard.BLACK
        self.assertEqual(board.get_possible_moves(ReversiBoard.WHITE),
                         [(2, 2), (2, 4), (6, 2), (6, 4)])

    def test_initial_str(self):
        initial_board = "\n" +\
            "    1   2   3   4   5   6   7   8  \n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "1 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "2 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "3 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "4 |   |   |   | O | X |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "5 |   |   |   | X | O |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "6 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "7 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "8 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n"

        board = ReversiBoard()

        self.maxDiff = None
        self.assertEqual(board.__str__(), initial_board)

    def test_several_moves_str(self):
        actual_board = "\n" +\
            "    1   2   3   4   5   6   7   8  \n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "1 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "2 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "3 |   |   |   | X | O |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "4 |   |   |   | O | O |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "5 |   |   | O | X | O |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "6 |   |   |   | X |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "7 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n" +\
            "8 |   |   |   |   |   |   |   |   |\n" +\
            "  +---+---+---+---+---+---+---+---+\n"

        board = ReversiBoard()
        board[2][3] = ReversiBoard.BLACK
        board[4][2] = ReversiBoard.WHITE
        board[5][3] = ReversiBoard.BLACK
        board[2][4] = ReversiBoard.WHITE

        self.maxDiff = None
        self.assertEqual(board.__str__(), actual_board)

    def test_initial_status(self):
        board = ReversiBoard()

        self.assertEqual(board.status, ReversiBoard.GAME_IN_PROGRESS)

    def test_in_progress_status(self):
        board = ReversiBoard()

        board[2][3] = ReversiBoard.BLACK
        board[4][2] = ReversiBoard.WHITE
        board[5][3] = ReversiBoard.BLACK
        board[2][4] = ReversiBoard.WHITE

        self.assertEqual(board.status, ReversiBoard.GAME_IN_PROGRESS)

    def test_white_wins_status(self):
        board = ReversiBoard()

        board[2][3] = ReversiBoard.BLACK
        board[2][2] = ReversiBoard.WHITE
        board[2][1] = ReversiBoard.BLACK
        board[1][1] = ReversiBoard.WHITE
        board[0][1] = ReversiBoard.BLACK
        board[0][0] = ReversiBoard.WHITE
        board[3][2] = ReversiBoard.BLACK
        board[0][2] = ReversiBoard.WHITE
        board[1][2] = ReversiBoard.BLACK
        board[1][3] = ReversiBoard.WHITE
        board[0][3] = ReversiBoard.BLACK
        board[0][4] = ReversiBoard.WHITE
        board[1][0] = ReversiBoard.BLACK
        board[2][0] = ReversiBoard.WHITE
        board[4][5] = ReversiBoard.BLACK
        board[1][4] = ReversiBoard.WHITE
        board[0][5] = ReversiBoard.BLACK
        board[0][6] = ReversiBoard.WHITE
        board.skip_player_move()
        board[1][5] = ReversiBoard.WHITE
        board.skip_player_move()
        board[2][4] = ReversiBoard.WHITE
        board.skip_player_move()
        board[4][1] = ReversiBoard.WHITE
        board[3][1] = ReversiBoard.BLACK
        board[4][0] = ReversiBoard.WHITE
        board[3][0] = ReversiBoard.BLACK
        board[4][2] = ReversiBoard.WHITE
        board[5][0] = ReversiBoard.BLACK
        board[3][5] = ReversiBoard.WHITE
        board[2][5] = ReversiBoard.BLACK
        board[2][6] = ReversiBoard.WHITE
        board[1][6] = ReversiBoard.BLACK
        board[1][7] = ReversiBoard.WHITE
        board[0][7] = ReversiBoard.BLACK
        board[2][7] = ReversiBoard.WHITE
        board[3][7] = ReversiBoard.BLACK
        board[3][6] = ReversiBoard.WHITE
        board[5][2] = ReversiBoard.BLACK
        board[4][6] = ReversiBoard.WHITE
        board[4][7] = ReversiBoard.BLACK
        board[5][1] = ReversiBoard.WHITE
        board[6][2] = ReversiBoard.BLACK
        board[5][3] = ReversiBoard.WHITE
        board[5][4] = ReversiBoard.BLACK
        board[5][5] = ReversiBoard.WHITE
        board[5][6] = ReversiBoard.BLACK
        board[5][7] = ReversiBoard.WHITE
        board[6][7] = ReversiBoard.BLACK
        board[6][0] = ReversiBoard.WHITE
        board.skip_player_move()
        board[6][1] = ReversiBoard.WHITE
        board[7][0] = ReversiBoard.BLACK
        board[6][3] = ReversiBoard.WHITE
        board[6][4] = ReversiBoard.BLACK
        board[6][5] = ReversiBoard.WHITE
        board[6][6] = ReversiBoard.BLACK
        board[7][6] = ReversiBoard.WHITE
        board[7][1] = ReversiBoard.BLACK
        board[7][2] = ReversiBoard.WHITE
        board[7][3] = ReversiBoard.BLACK
        board[7][4] = ReversiBoard.WHITE
        board[7][5] = ReversiBoard.BLACK
        board.skip_player_move()
        board[7][7] = ReversiBoard.BLACK

        self.assertEqual(board.status, ReversiBoard.WHITE_WINS)

    def test_black_wins_status(self):
        board = ReversiBoard()

        board._board = [[' ' for _ in range(0, ReversiBoard.BOARD_SIZE)]
                        for _ in range(0, ReversiBoard.BOARD_SIZE)]
        board._board[0][0] = ReversiBoard.BLACK
        board._board[0][1] = ReversiBoard.BLACK
        board._board[5][5] = ReversiBoard.WHITE
        board._last_move = ReversiBoard.BLACK
        board.update_status()

        self.assertEqual(board.status, ReversiBoard.BLACK_WINS)

    def test_draw_status(self):
        board = ReversiBoard()

        board._board = [[' ' for _ in range(0, ReversiBoard.BOARD_SIZE)]
                        for _ in range(0, ReversiBoard.BOARD_SIZE)]
        board._board[0][0] = ReversiBoard.BLACK
        board._board[5][5] = ReversiBoard.WHITE
        board._last_move = ReversiBoard.WHITE
        board.update_status()

        self.assertEqual(board.status, ReversiBoard.DRAW)

if __name__ == '__main__':
    from reversi_board import *
    unittest.main()
else:
    from .reversi_board import *
