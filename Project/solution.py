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

    ROW_NUMBERS = [str(number)
                   for number
                   in range(1, self.BOARD_SIZE + 1)]
    COLUMN_LETTERS = ascii_uppercase[0:self.BOARD_SIZE]

    BLACK = 'B'
    WHITE = 'W'

    VALUES = [self.BLACK, self.WHITE]
    GAME_IN_PROGRESS = 'Game in progress.'
    TIES = 'Ties!'
    WHITE_WINS = 'White wins!'
    BLACK_WINS = 'Black wins!'

    class ReversiBoardLine:

        def __init__(self):
            self.boardLine = dict()

        def __getitem__(self, key):
            if key not in ReversiBoard.COLUMN_LETTERS:
                raise InvalidKey
            return self.boardLine.get(key, '')

        def __setitem__(self, key, value):
            if key not in ReversiBoard.COLUMN_LETTERS:
                raise InvalidIndex
            elif key in self.boardLine:
                raise InvalidMove
            self.boardLine[key] = value

    def __init__(self):
        self.board = dict()
        for i in self.ROW_NUMBERS:
            self.board[i] = ReversiBoardLine()

        self.status = self.GAME_IN_PROGRESS
        self.last_move = None

    def __getitem__(self, key):
        if key not in self.ROW_NUMBERS:
            raise InvalidKey
        return self.board[key]

    def update_game_status(self):
        pass

    def __str__(self):
        pass

    def game_status(self):
        return game_status
