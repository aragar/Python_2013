class TicTacToeBoard:

    def __init__(self):
        self.board = dict()

    def __getitem__(self, key):
        print(self.board[key])

    def __setitem__(self, key, value):
        self.board[key] = value

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