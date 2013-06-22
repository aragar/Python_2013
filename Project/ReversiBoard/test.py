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

if __name__ == '__main__':
    from ReversiBoard import *
    unittest.main()
else:
    from .ReversiBoard import *
