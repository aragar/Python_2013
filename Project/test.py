import unittest
from solution import *


class TestConstants(unittest.TestCase):

    def test_board_size(self):
        board = ReversiBoard()
        self.assertEqual(board.BOARD_SIZE, 8)

    def test_board_column_names(self):
        board = ReversiBoard()
        self.assertEqual(board.COLUMN_NUMBERS, [
                         '8', '7', '6', '5', '4', '3', '2', '1'])

    def test_board_row_names(self):
        board = ReversiBoard()
        self.assertEqual(board.ROW_LETTERS, "ABCDEFGH")


if __name__ == '__main__':
    unittest.main()
