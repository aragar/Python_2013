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
    BOARD_SIZE = 8

    COLUMN_NUMBERS = [str(number) for number in range(BOARD_SIZE, 0, -1)]
    ROW_LETTERS = ascii_uppercase[0:BOARD_SIZE]

    BLACK = 0
    WHITE = 1

    VALUES = [BLACK, WHITE]
    GAME_IN_PROGRESS = 'Game in progress.'
    TIES = 'Ties!'
    WHITE_WINS = 'White wins!'
    BLACK_WINS = 'Black wins!'

    def __init__(self):
        pass

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
