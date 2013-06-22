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

    def __init__(self):
        self._board = [["" for _ in range(0, self.BOARD_SIZE)]
                       for _ in range(0, self.BOARD_SIZE)]

        self._board[3][4] = ReversiBoard.BLACK
        self._board[3][3] = ReversiBoard.WHITE
        self._board[4][3] = ReversiBoard.BLACK
        self._board[4][4] = ReversiBoard.WHITE

        self.last_move = self.WHITE  # Blacks are first to play

    def __getitem__(self, key):
        if key not in range(0, self.BOARD_SIZE):
            raise InvalidKey

        row = self._board[key]
        row_number = key
        _board = self

        # Generates a class, which modifies this row
        class ReversiBoardLine:

            def __getitem__(self, key):
                if key not in range(0, ReversiBoard.BOARD_SIZE):
                    raise InvalidKey

                return row[key]

            def __setitem__(self, key, value):
                if key not in range(0, ReversiBoard.BOARD_SIZE):
                    raise InvalidKey
                elif row[key] in ReversiBoard.PLAYERS:
                    raise InvalidMove
                elif value not in ReversiBoard.PLAYERS:
                    raise InvalidValue
                elif value == _board.last_move:
                    raise NotYourTurn
                elif (row_number, key) not in _board.get_possible_moves(value):
                    raise InvalidMove
                else:
                    row[key] = value
                    _board.update_game(row_number, key)
                    _board.last_move = value

        return ReversiBoardLine()

    def get_possible_moves(self, player):
        possible_moves = [(x, y)
                          for x in range(0, self.BOARD_SIZE)
                          for y in range(0, self.BOARD_SIZE)
                          if (self._board[x][y] not in self.PLAYERS and
                              len(self.get_cells_to_flip(x, y, player)) > 0)]

        return possible_moves

    def get_cells_to_flip(self, x, y, player):
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
                       self._board[new_x][new_y] and
                       self._board[new_x][new_y] != player):
                    opposites_line.append((new_x, new_y))
                    new_x += DX[delta]
                    new_y += DY[delta]

                if (new_x in range(0, self.BOARD_SIZE) and
                    new_y in range(0, self.BOARD_SIZE) and
                    self._board[new_x][new_y] == player and
                        len(opposites_line) > 0):
                    opposites.extend(opposites_line)

        return opposites

    def update_game(self, x, y):
        if (x not in range(0, self.BOARD_SIZE) or
                y not in range(0, self.BOARD_SIZE)):
            raise InvalidKey

        if self._board[x][y] not in self.PLAYERS:
            raise InvalidValue

        player = self._board[x][y]
        opposites = self.get_cells_to_flip(x, y, player)

        for (x, y) in opposites:
            self._board[x][y] = player

    def __str__(self):
        HLINE = '  ' + ('+---' * self.BOARD_SIZE) + '+'
        NLINE = '  ' + ('  {} ' * self.BOARD_SIZE).format(
            *range(1, self.BOARD_SIZE + 1)) + ' '

        representaion = '\n'
        representaion += NLINE + '\n'
        representaion += HLINE + '\n'
        for x in range(self.BOARD_SIZE):

            representaion += '{} '.format(x + 1)
            for y in range(self.BOARD_SIZE):
                representaion += '| {} '.format(self._board[
                                                x][y] if self._board[x][y] else ' ')
            representaion += '|\n'

            representaion += HLINE + '\n'

        # print(representaion)
        return representaion
