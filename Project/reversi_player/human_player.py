from reversi_player.player import Player
from reversi_game.constants import ReversiGameConstants
from reversi_board.reversi_board import ReversiBoard, InvalidKey, InvalidMove


class HumanPlayer(Player):

    def move(self):
        can_player_move = self._board.can_player_move(self._color)

        if not can_player_move:
            self._board.skip_player_move()
            print("Sorry, You can't move.")
            return ReversiGameConstants.SKIP

        while True:
            move = input('--> ').lower().split()
            print(move)

            if len(move) == 2:
                try:
                    x = int(move[0]) - 1
                    y = int(move[1]) - 1
                    self._board[x][y] = self._color
                    break
                except (ValueError, InvalidKey):
                    print("Invalid coordinates. Please enter only numbers from 1 to " + \
                        str(ReversiBoard.BOARD_SIZE) + \
                        "inclusively.")
                except InvalidMove:
                    print("Invalid move. You can't place a piece there.")
                except:
                    print("Please, enter a pair of valid coordinates.")
            elif len(move) == 1 and move[0] == ReversiGameConstants.QUIT:
                return ReversiGameConstants.QUIT
            else:
                print("Please, enter a pair of valid coordinates.")
