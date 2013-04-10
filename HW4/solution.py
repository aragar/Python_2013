class TicTacToeBoard:

    def __init__(self):
        self.board = dict()

    def __getitem__(self, key):
        print(self.board[key])

    def __setitem__(self, key, value):
        self.board[key] = value
