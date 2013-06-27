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
    COORDINATE = list(range(1, BOARD_SIZE + 1))

    WHITE = 'O'
    BLACK = 'X'
    EMPTY = ' '
    PLAYERS = [WHITE, BLACK]
    OPPOSITE = {WHITE: BLACK, BLACK: WHITE}

    GAME_IN_PROGRESS = 0
    BLACK_WINS = 1
    WHITE_WINS = 2
    DRAW = 3

    def __init__(self):
        self._board = [[self.EMPTY for _ in range(0, self.BOARD_SIZE)]
                       for _ in range(0, self.BOARD_SIZE)]

        if self.BOARD_SIZE > 2:
            half_size = int(self.BOARD_SIZE / 2)
            self._board[half_size - 1][half_size] = ReversiBoard.BLACK
            self._board[half_size - 1][half_size - 1] = ReversiBoard.WHITE
            self._board[half_size][half_size - 1] = ReversiBoard.BLACK
            self._board[half_size][half_size] = ReversiBoard.WHITE

        self._last_move = self.WHITE  # Blacks are first to play
        self.status = self.GAME_IN_PROGRESS

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
                elif value == _board._last_move:
                    raise NotYourTurn
                elif (row_number, key) not in _board.get_possible_moves(value):
                    raise InvalidMove
                else:
                    row[key] = value
                    _board.update_game(row_number, key)
                    _board._last_move = value
                    _board.update_status()

        return ReversiBoardLine()

    def get_possible_moves(self, player):
        possible_moves = [(x, y)
                          for x in range(0, self.BOARD_SIZE)
                          for y in range(0, self.BOARD_SIZE)
                          if (self._board[x][y] == self.EMPTY and
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
                       self._board[new_x][new_y] == self.OPPOSITE[player]):
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

    def update_status(self):
        if self.status != self.GAME_IN_PROGRESS:
            return

        player = self.OPPOSITE[self._last_move]
        opponent = self.OPPOSITE[player]

        can_player_move = self.can_player_move(player)
        can_opponent_move = self.can_player_move(opponent)

        if not can_player_move and not can_opponent_move:
            black_pieces = self.get_number_of_pieces(self.BLACK)
            white_pieces = self.get_number_of_pieces(self.WHITE)

            if black_pieces > white_pieces:
                self.status = self.BLACK_WINS
            elif white_pieces > black_pieces:
                self.status = self.WHITE_WINS
            else:
                self.status = self.DRAW

    def get_number_of_pieces(self, player):
        return sum(self._board[i].count(player)
                   for i in range(0, self.BOARD_SIZE))

    def can_player_move(self, player):
        return len(self.get_possible_moves(player)) > 0

    def skip_player_move(self):
        self._last_move = self.OPPOSITE[self._last_move]

    def copy(self):
        copy_board = ReversiBoard()

        copy_board._board = [self._board[i][j]
                             for i in range(0, self.BOARD_SIZE)
                             for j in range(0, self.BOARD_SIZE)]
        copy_board._last_move = self._last_move
        copy_board.status = self.status

        return copy_board

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
                representaion += '| {} '.format(self._board[x][y])
            representaion += '|\n'

            representaion += HLINE + '\n'

        return representaion
