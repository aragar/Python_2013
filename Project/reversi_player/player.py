from reversi_board.reversi_board import ReversiBoard


class Player:

    def __init__(self, board, color):
        self._board = board
        self._color = color

    def move(self):
        pass

    def get_color(self):
    	return self._color

    def get_board(self):
    	return self._board.copy()
