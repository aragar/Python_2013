from os import system

from ReversiBoard.ReversiBoard import ReversiBoard, InvalidKey, InvalidMove


class ReversiGame:

    def __init__(self):
        self.board = ReversiBoard()

    def __call__(self):
        while True:
            print(self.board)
            self.player_move()

            print(self.board)
            self.ai_move()

    def player_move(self):
        while True:
            move = input('--> ').lower().split()
            print(move)

            if (len(move) == 2 and
                int(move[0]) in ReversiBoard.COORDINATE and
                    int(move[1]) in ReversiBoard.COORDINATE):
                x = int(move[0]) - 1
                y = int(move[1]) - 1
                try:
                    self.board[x][y] = ReversiBoard.BLACK
                    break
                except InvalidKey:
                    print("Please, enter valid coordinates.")
                except InvalidMove:
                    print(
                        "This cell is occupied. Please, enter free coordinates.")
            else:
                print("Fuck you!")

    def ai_move(self):
        possible_moves = self.board.get_possible_moves(ReversiBoard.WHITE)
        x, y = possible_moves[0]

        self.board[x][y] = ReversiBoard.WHITE


if __name__ == '__main__':
    ReversiGame().__call__()
