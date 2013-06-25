from reversi_board.reversi_board import ReversiBoard


class TrivialAI:

    @staticmethod
    def generate_move(board, player):
        possible_moves = board.get_possible_moves(player)

        return possible_moves[0]
