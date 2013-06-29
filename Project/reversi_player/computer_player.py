from reversi_player.player import Player
from reversi_ai.trivial_ai import TrivialAI
from reversi_ai.greedy_ai import GreedyAI
from reversi_ai.alphabeta_ai import AlphaBetaAI
from reversi_game.constants import ReversiGameConstants


class ComputerPlayer(Player):

    def __init__(self, board, color):
        super().__init__(board, color)
        self._alphabeta_ai = AlphaBetaAI(self, 4)

    def move(self):
        can_computer_move = self._board.can_player_move(self._color)

        if not can_computer_move:
            self._board.skip_player_move()
            print("The computer can't move.")
            return ReversiGameConstants.SKIP

        x, y = self._alphabeta_ai.generate_move()
        print("Computer's move: {}, {}".format(x + 1, y + 1))
        self._board[x][y] = self._color
