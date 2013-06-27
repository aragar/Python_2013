from os import system

from reversi_board.reversi_board import *
from reversi_ai.trivial_ai import TrivialAI
from reversi_ai.greedy_ai import GreedyAI


class ReversiGame:

    QUIT = 'quit'
    SKIP = 'skip'

    def __init__(self):
        self.board = ReversiBoard()

    def __call__(self):
        while True:
            if self.board.status != ReversiBoard.GAME_IN_PROGRESS:
                break

            if self.board.can_player_move(ReversiBoard.BLACK):
                print(self.board)
                print("Possible moves: " + str(
                    [(x + 1, y + 1)
                     for x, y
                     in self.board.get_possible_moves(self.board.BLACK)]))
                print("Current game status: " + str(self.board.status))
                print("Black's pieces: " + str(
                    self.board.get_number_of_pieces(self.board.BLACK)))
                print("White's pieces: " + str(
                    self.board.get_number_of_pieces(self.board.WHITE)))

                result = self.player_move()
                if result == self.QUIT:
                    break
            else:
                self.board.skip_player_move()

            if self.board.status != ReversiBoard.GAME_IN_PROGRESS:
                break

            if self.board.can_player_move(ReversiBoard.WHITE):
                print(self.board)
                self.ai_move()
            else:
                self.board.skip_player_move()

        print(self.board)
        if self.board.status == ReversiBoard.BLACK_WINS:
            print("YOU WIN !!! ... WTF!? HOW!?")
        elif self.board.status == ReversiBoard.WHITE_WINS:
            print("YOU LOSE !!! ... which was quite expected ^_^")
        elif self.board.status == ReversiBoard.DRAW:
            print("IT'S A DRAW !!! ... You should be quite lucky about that.")
        else:
            print("End ... er's game!")

    def player_move(self):

        if not self.board.can_player_move(ReversiBoard.BLACK):
            self.board.skip_player_move()
            return self.SKIP

        while True:
            move = input('--> ').lower().split()
            print(move)

            if len(move) == 2:
                try:
                    x = int(move[0]) - 1
                    y = int(move[1]) - 1
                    self.board[x][y] = ReversiBoard.BLACK
                    break
                except:
                    print("Please, enter valid coordinates.")
            elif len(move) == 1 and move[0] == self.QUIT:
                return self.QUIT
            else:
                print("Fuck you!")

    def ai_move(self):
        if not self.board.can_player_move(ReversiBoard.WHITE):
            self.board.skip_player_move()
            return self.SKIP

        x, y = TrivialAI.generate_move(self.board, ReversiBoard.WHITE)
        self.board[x][y] = ReversiBoard.WHITE


if __name__ == '__main__':
    ReversiGame().__call__()
