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

    def test_board_keys(self):
        board = ReversiBoard()
        keys = ['A8', 'A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1',
                'B8', 'B7', 'B6', 'B5', 'B4', 'B3', 'B2', 'B1',
                'C8', 'C7', 'C6', 'C5', 'C4', 'C3', 'C2', 'C1',
                'D8', 'D7', 'D6', 'D5', 'D4', 'D3', 'D2', 'D1',
                'E8', 'E7', 'E6', 'E5', 'E4', 'E3', 'E2', 'E1',
                'F8', 'F7', 'F6', 'F5', 'F4', 'F3', 'F2', 'F1',
                'G8', 'G7', 'G6', 'G5', 'G4', 'G3', 'G2', 'G1',
                'H8', 'H7', 'H6', 'H5', 'H4', 'H3', 'H2', 'H1',]
        self.assertEqual(board.KEYS, keys)


if __name__ == '__main__':
    unittest.main()
