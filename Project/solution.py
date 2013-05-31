from string import ascii_uppercase


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class ReversiBoard:

    def __init__(self):
        self.BOARD_SIZE = 8

        self.COLUMN_NUMBERS = [str(number)
                               for number
                               in range(1, self.BOARD_SIZE + 1)]
        self.ROW_LETTERS = ascii_uppercase[0:self.BOARD_SIZE]

        self.BLACK = 'B'
        self.WHITE = 'W'

        self.VALUES = [self.BLACK, self.WHITE]
        self.GAME_IN_PROGRESS = 'Game in progress.'
        self.TIES = 'Ties!'
        self.WHITE_WINS = 'White wins!'
        self.BLACK_WINS = 'Black wins!'

        self.KEYS = [row + column
                     for row in self.ROW_LETTERS
                     for column in self.COLUMN_NUMBERS]

        self.board = dict()
        self.status = self.GAME_IN_PROGRESS
        self.last_move = None

    def __getitem__(self, key):
        return self.board.get(key, ' ')

    def __setitem__(self, key, value):
        if key in self.board:
            raise InvalidMove
        elif key not in self.KEYS:
            raise InvalidKey
        elif value not in self.VALUES:
            raise InvalidValue
        elif value == self.last_move:
            raise NotYourTurn
        else:
            self.board[key] = value
            self.last_move = value
            self.update_game_status()

    def update_game_status(self):
        pass

    def __str__(self):
        pass

    def game_status(self):
        return game_status
