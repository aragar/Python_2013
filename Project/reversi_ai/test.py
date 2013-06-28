import unittest

from reversi_ai.alphabeta_ai import AlphaBetaAI
from reversi_ai.greedy_ai import GreedyAI
from reversi_ai.trivial_ai import TrivialAI
from reversi_player.computer_player import ComputerPlayer
from reversi_board.reversi_board import ReversiBoard


def _make_a_board():
    board = ReversiBoard()

    board._board = [[ReversiBoard.BLACK
                     for _ in range(0, 8)]
                    for _ in range(0, 8)]

    board._board[7][0] = ReversiBoard.EMPTY
    board._board[5][1] = ReversiBoard.EMPTY
    board._board[5][2] = ReversiBoard.EMPTY

    board._board[2][1] = ReversiBoard.WHITE
    board._board[2][2] = ReversiBoard.WHITE
    board._board[2][3] = ReversiBoard.WHITE
    board._board[2][4] = ReversiBoard.WHITE
    board._board[2][6] = ReversiBoard.WHITE
    board._board[3][2] = ReversiBoard.WHITE
    board._board[3][4] = ReversiBoard.WHITE
    board._board[3][5] = ReversiBoard.WHITE
    board._board[3][7] = ReversiBoard.WHITE
    board._board[4][4] = ReversiBoard.WHITE
    board._board[4][6] = ReversiBoard.WHITE
    board._board[4][7] = ReversiBoard.WHITE
    board._board[5][4] = ReversiBoard.WHITE
    board._board[5][6] = ReversiBoard.WHITE
    board._board[6][2] = ReversiBoard.WHITE
    board._board[6][5] = ReversiBoard.WHITE
    board._board[7][1] = ReversiBoard.WHITE
    board._board[7][2] = ReversiBoard.WHITE

    board.status = ReversiBoard.GAME_IN_PROGRESS
    board._last_move = ReversiBoard.BLACK

    return board


class TestAlphaBetaAI(unittest.TestCase):

    def test_generate_move(self):
        board = _make_a_board()

        player = ComputerPlayer(board, ReversiBoard.WHITE)
        alphabeta = AlphaBetaAI(player, 3)
        x, y = alphabeta.generate_move()

        self.assertEqual((x, y), (5, 2))


class TestTrivialAI(unittest.TestCase):

    def test_generate_move(self):
        board = _make_a_board()

        x, y = TrivialAI.generate_move(board, ReversiBoard.WHITE)

        self.assertEqual((x, y), (5, 1))


class TestGreedyAI(unittest.TestCase):

    def test_generate_move(self):
        board = _make_a_board()

        x, y = GreedyAI.generate_move(board, ReversiBoard.WHITE)

        self.assertEqual((x, y), (5, 1))
