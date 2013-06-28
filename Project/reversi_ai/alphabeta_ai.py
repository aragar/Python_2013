from sys import maxsize

from reversi_board.reversi_board import ReversiBoard


class AlphaBetaAI:

    MAX_BOARD_VALUE = maxsize
    MIN_BOARD_VALUE = -maxsize

    def __init__(self, player, max_depth=1):
        self._player = player
        self._max_depth = max_depth

    def generate_move(self):
        return self._generate_alphabeta_move(self._player.get_board(), True,
                                             1, self.MIN_BOARD_VALUE,
                                             self.MAX_BOARD_VALUE)[1:]

    def _generate_alphabeta_move(self, board, is_maximizing, current_depth, alpha, beta):
        initial_player = self._player.get_color()
        current_player = initial_player if is_maximizing else ReversiBoard.OPPOSITE[initial_player]
        player_skips_move = False
        possible_moves = []

        is_final_move = current_depth > self._max_depth

        if not is_final_move:
            possible_moves = board.get_possible_moves(current_player)

            if not board.can_player_move(current_player):
                player_skips_move = True
                opposite = ReversiBoard.OPPOSITE[current_player]
                
                possible_moves = board.get_possible_moves(opposite)
                current_player = opposite

                isFinalMove = board.can_player_move(opposite)

        if is_final_move:
            result_x = -1
            result_y = -1
            result = self._evaluate_board(board)

            return (result, result_x, result_y)
        else:
            best_value = self.MIN_BOARD_VALUE if is_maximizing else self.MAX_BOARD_VALUE
            best_x = -1
            best_y = -1

            for x, y in possible_moves:
                next_board = board.copy()

                if player_skips_move:
                    next_board.skip_player_move();
                next_board[x][y] = current_player

                next_is_maximazing = is_maximizing if player_skips_move else not is_maximizing

                current_value = self._generate_alphabeta_move(next_board,
                                                              next_is_maximazing,
                                                              current_depth + 1,
                                                              alpha, beta)[0]
                if is_maximizing and current_value > best_value:
                    best_value = current_value
                    best_x = x
                    best_y = y

                    if best_value > alpha:
                        alpha = best_value

                    if best_value >= beta:
                        break
                elif not is_maximizing and current_value < best_value:
                    best_value = current_value
                    best_x = x
                    best_y = y

                    if best_value < beta:
                        beta = best_value

                    if best_value <= alpha:
                        break

            result_x = best_x
            result_y = best_y
            return (best_value, result_x, result_y)

    def _evaluate_board(self, board):
        player = self._player.get_color()
        opponent = ReversiBoard.OPPOSITE[player]

        can_player_move = board.can_player_move(player)
        can_opponent_move = board.can_player_move(opponent)

        if not can_player_move and not can_opponent_move:
            player_pieces = board.get_number_of_pieces(player)
            opponent_pieces = board.get_number_of_pieces(opponent)
            result = player_pieces - opponent_pieces

            # it is a terminal state, so the result should be much
            # larger/smaller
            addend = board.BOARD_SIZE ** 4 + board.BOARD_SIZE ** 3
            if result < 0:
                addend = -addend

            return result + addend

        else:
                # heuristic function, based on eventual number of pieces to be
                # got
            player_possible_moves = board.get_possible_moves(player)
            player_flips = sum(len(board.get_cells_to_flip(x, y, player))
                               for x, y in player_possible_moves)

            opponent_possible_moves = board.get_possible_moves(opponent)
            opponent_flips = sum(len(board.get_cells_to_flip(x, y, opponent))
                                 for x, y in opponent_possible_moves)

            return player_flips - opponent_flips
