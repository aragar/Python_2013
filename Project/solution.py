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
                               in range(self.BOARD_SIZE, 0, -1)]
        self.ROW_LETTERS = ascii_uppercase[0:self.BOARD_SIZE]

        self.BLACK = 0
        self.WHITE = 1

        self.VALUES = [self.BLACK, self.WHITE]
        self.GAME_IN_PROGRESS = 'Game in progress.'
        self.TIES = 'Ties!'
        self.WHITE_WINS = 'White wins!'
        self.BLACK_WINS = 'Black wins!'

        self.KEYS = [row + column
                     for row in self.ROW_LETTERS
                     for column in self.COLUMN_NUMBERS]

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def update_game_status(self):
        pass

    def __str__(self):
        pass

    def game_status(self):
        pass
