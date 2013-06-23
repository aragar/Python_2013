from ReversiBoard.ReversiBoard import ReversiBoard


class GreedyAI:

    @staticmethod
    def generate_move(cls, board, player):
        possible_moves = board.get_possible_moves(player)

        best_score = -1
        for x, y in possible_moves:
            copy_board = board.copy()

            copy_board[x][y] = player
            score = copy_board.get_number_of_pieces(player)
            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move
