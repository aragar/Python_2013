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
                self.board.update_game(self.row, key)
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
                          if len(self.get_opposites(x, y, player)) > 0]

        return possible_moves

    def get_opposites(self, x, y, player):
        opposites = []

        if (x in range(0, self.BOARD_SIZE) and
            y in range(0, self.BOARD_SIZE) and
                player in self.PLAYERS):
            DX = [1, 1, 0, -1, -1, -1, 0, 1]
            DY = [0, -1, -1, -1, 0, 1, 1, 1]

            for delta in range(0, self.BOARD_SIZE):
                opposites_line = []

                new_x = x + DX[delta]
                new_y = y + DY[delta]
                while (new_x in range(0, self.BOARD_SIZE) and
                       new_y in range(0, self.BOARD_SIZE) and
                       self.board[new_x][new_y] and
                       self.board[new_x][new_y] != player):
                    opposites_line.append((new_x, new_y))
                    new_x += DX[delta]
                    new_y += DY[delta]

                if (new_x in range(0, self.BOARD_SIZE) and
                    new_y in range(0, self.BOARD_SIZE) and
                    self.board[new_x][new_y] == player and
                        len(opposites_line) > 0):
                    opposites.extend(opposites_line)

        return opposites

    def update_game(self, x, y):
        pass
