import unittest
from ReversiBoard import *


class TestReversiBoard(unittest.TestCase):

    def test_board_size(self):
        board = ReversiBoard()
        self.assertEqual(board.BOARD_SIZE, 8)

    def test_invalid_value_exception_raises(self):
        invalid_value = ReversiBoard()
        with self.assertRaises(InvalidValue):
            invalid_value[1][1] = "F"

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
            not_your_turn[0][0] = "X"
            not_your_turn[0][1] = "X"

if __name__ == '__main__':
    unittest.main()
