class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class ReversiBoard:
    BOARD_SIZE = 8

    WHITE = 'O'
    BLACK = 'X'

    PLAYERS = [WHITE, BLACK]

    class ReversiBoardLine:

        def __init__(self, board, row):
            self.board = board
            self.row = row
            self.board_line = dict()

            if row == 3:
                self.board_line[3] = ReversiBoard.WHITE
                self.board_line[4] = ReversiBoard.BLACK
            elif row == 4:
                self.board_line[3] = ReversiBoard.BLACK
                self.board_line[4] = ReversiBoard.WHITE

        def __getitem__(self, key):
            if key not in range(0, ReversiBoard.BOARD_SIZE):
                raise InvalidKey
            return self.board_line.get(key, '')

        def __setitem__(self, key, value):
            if key not in range(0, ReversiBoard.BOARD_SIZE):
                raise InvalidKey
            elif key in self.board_line:
                raise InvalidMove
            elif value not in ReversiBoard.PLAYERS:
                raise InvalidValue
            elif value == self.board.last_move:
                raise NotYourTurn
            elif (self.row, key) not in self.board.get_possible_moves(value):
               raise InvalidMove
            else:
                self.board_line[key] = value
                self.board.last_move = value

    def __init__(self):
        self.board = [self.ReversiBoardLine(self, row)
                      for row
                      in range(0, self.BOARD_SIZE)]
        self.last_move = self.WHITE  # Blacks are first to play

    def __getitem__(self, key):
        if key not in range(0, self.BOARD_SIZE):
            raise InvalidKey
        return self.board[key]

    def get_possible_moves(self, player):
        possible_moves = [(x, y)
                          for x in range(0, self.BOARD_SIZE)
                          for y in range(0, self.BOARD_SIZE)
                          if self.check_move_possible(x, y, player)]

        return possible_moves

    def check_move_possible(self, x, y, player):
        if x not in range(0, self.BOARD_SIZE) or y not in range(0, self.BOARD_SIZE):
            return False

        if player not in self.PLAYERS:
            return False

        if self.board[x][y]:
            return False

        DX = [1, 1, 0, -1, -1, -1, 0, 1]
        DY = [0, -1, -1, -1, 0, 1, 1, 1]

        for delta in range(0, self.BOARD_SIZE):
            new_x = x + DX[delta]
            new_y = y + DY[delta]
            while (new_x in range(0, self.BOARD_SIZE) and
                   new_y in range(0, self.BOARD_SIZE) and
                   self.board[new_x][new_y] and
                   self.board[new_x][new_y] != player):
                new_x += DX[delta]
                new_y += DY[delta]

            if (new_x in range(0, self.BOARD_SIZE) and
                new_y in range(0, self.BOARD_SIZE) and
                self.board[new_x][new_y] == player and
                    (new_x - x != DX[delta] or new_y - y != DY[delta])):
                return True

        return False
