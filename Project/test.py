import unittest
from ReversiBoard import *


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
            invalid_key[2][10] = "X"

    def test_invalid_move_exception_raises(self):
        invalid_move = ReversiBoard()
        with self.assertRaises(InvalidMove):
            invalid_move[0][0] = "X"
            invalid_move[0][0] = "O"

    def test_not_your_turn_exception_raises(self):
        not_your_turn = ReversiBoard()
        with self.assertRaises(NotYourTurn):
            not_your_turn[2][3] = "X"
            not_your_turn[5][2] = "X"

    def test_possible_moves(self):
        board = ReversiBoard()
        possible_moves = board.get_possible_moves(ReversiBoard.BLACK)
        self.assertEqual(possible_moves, [(2, 3), (3, 2), (4, 5), (5, 4)])

    def test_get_opposites(self):
        board = ReversiBoard()
        self.assertEqual(board.get_opposites(2, 3, ReversiBoard.BLACK),
                         [(3, 3)])

    def test_get_no_opposites(self):
        board = ReversiBoard()
        self.assertEqual(board.get_opposites(1, 1, ReversiBoard.BLACK),
                         [])

    def test_invalid_move_exception_raises_move_not_possible(self):
        move_not_possible = ReversiBoard()
        with self.assertRaises(InvalidMove):
            move_not_possible[1][1] = ReversiBoard.BLACK

if __name__ == '__main__':
    unittest.main()
