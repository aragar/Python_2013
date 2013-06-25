from reversi_board.reversi_board import ReversiBoard


class GreedyAI:

    @staticmethod
    def generate_move(board, player):
        possible_moves = board.get_possible_moves(player)

        best_score = -1
        for x, y in possible_moves:
            score = len(board.get_cells_to_flip(x, y, player))

            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move
