from os import system

from reversi_board.reversi_board import ReversiBoard
from reversi_player.human_player import HumanPlayer
from reversi_player.computer_player import ComputerPlayer
from reversi_game.constants import ReversiGameConstants


class ReversiGame:

    def __init__(self):
        self._board = ReversiBoard()

        self._human = HumanPlayer(self._board, ReversiBoard.BLACK)
        self._computer = ComputerPlayer(self._board, ReversiBoard.WHITE)

        self._current_player = self._human

    def __call__(self):
        while True:
            print(self._board)
            print("Possible moves: " +
                  str([(x + 1, y + 1)
                       for x, y
                       in self._board.get_possible_moves(self._current_player.get_color())]))
            print("Black's: " +
                  str(self._board.get_number_of_pieces(ReversiBoard.BLACK)))
            print("White's: " +
                  str(self._board.get_number_of_pieces(ReversiBoard.WHITE)))

            player_move = self._current_player.move()

            if player_move == ReversiGameConstants.QUIT:
                break

            if self._board.status != ReversiBoard.GAME_IN_PROGRESS:
                break

            self._current_player = self.next_player()

        print(self._board)
        if self.board.status == self._human._color:
            print("YOU WIN !!! ... WTF!? HOW!?")
        elif self.board.status == self._computer._color:
            print("YOU LOSE !!! ... which was quite expected ^_^")
        elif self.board.status == ReversiBoard.DRAW:
            print("IT'S A DRAW !!! ... You should be quite lucky about that.")
        else:
            print("End!")

    def next_player(self):
        if self._current_player is self._human:
            next_player = self._computer
        else:
            next_player = self._human

        return next_player

if __name__ == '__main__':
    ReversiGame().__call__()
