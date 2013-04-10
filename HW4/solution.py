class InvalidMove(Exception):
    pass

class InvalidValue(Exception):
    pass

class InvalidKey(Exception):
    pass

class NotYourTurn(Exception):
    pass

class TicTacToeBoard:

    def __init__(self):
        self.board = dict()
        self._last = 'RADO'

    def __getitem__(self, key):
        print(self.board[key])

    def __setitem__(self, key, value):
        if key in self.board:
            raise InvalidMove
        elif key not in [column + row for row in '123' for column in 'ABC']:
            raise InvalidKey
        elif value not in ['X', 'O']:
            raise InvalidValue
        elif value == self._last:
            raise NotYourTurn
        else:
            self.board[key] = value
            self._last = value

    def __str__(self):
        return ('\n' +\
            '  -------------\n' +\
            '3 | {} | {} | {} |\n' +\
            '  -------------\n' +\
            '2 | {} | {} | {} |\n' +\
            '  -------------\n' +\
            '1 | {} | {} | {} |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n').format(*[self.board.get(column + row, " ")
                                        for row in '321'
                                        for column in 'ABC'])