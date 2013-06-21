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

    WHITE_PLAYER = 'O'
    BLACK_PLAYER = 'X'

    PLAYERS = [WHITE_PLAYER, BLACK_PLAYER]

    class ReversiBoardLine:

        def __init__(self, board):
            self.board = board
            self.boardLine = dict()

        def __getitem__(self, key):
            if key not in range(0, ReversiBoard.BOARD_SIZE):
                raise InvalidKey
            return self.boardLine.get(key, '')

        def __setitem__(self, key, value):
            if key not in range(0, ReversiBoard.BOARD_SIZE):
                raise InvalidKey
            elif key in self.boardLine:
                raise InvalidMove
            elif value not in ReversiBoard.PLAYERS:
                raise InvalidValue
            elif value == self.board.last_move:
                raise NotYourTurn
            else:
                self.boardLine[key] = value
                self.board.last_move = value

    def __init__(self):
        self.board = [self.ReversiBoardLine(self) for _ in range(0, self.BOARD_SIZE)]
        self.last_move = self.WHITE_PLAYER # Blacks are first to play

    def __getitem__(self, key):
        if key not in range(0, self.BOARD_SIZE):
            raise InvalidKey
        return self.board[key]
