from connectfour.agents.computer_player import RandomAgent
import random
import pdb

SEVENTH_COLUMN = 6

FIRST_COLUMN = 0

FIFTH_COLUMN = 5

SIXTH_COLUMN = 5

SECOND_COLUMN = 1

THIRD_COLUMN = 2

MIDDLE_COLUMN = 3

TWO_VALUE = 10

TWO_IN_ROW = 2

WINDOW_LENGTH = 4

THREE_VALUE = 100

LOSE_VALUE = -1000000000000000

THREE_IN_ROW = 3

FOUR_IN_ROW = 4

WIN_VALUE = 1000000000000000


class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 2
        # if self.id == 1:
        #     self.opponent_id = 2
        # elif self.id == 2:
        #     self.opponent_id = 1
        # self.opponent_id = int(self.id, 10) % 3

    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append(move)
            vals.append(self.dfMiniMax(next_state, 1))

        bestMove = moves[vals.index(max(vals))]
        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])

            moves.append(move)
            vals.append(self.dfMiniMax(next_state, depth + 1))

        if depth % 2 == 1:
            bestVal = min(vals)
        else:
            bestVal = max(vals)

        return bestVal

    def evaluateBoardState(self, board):
        """
        Your evaluation function should look at the current state and return a score for it. 
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width 
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array 
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """
        # valid_moves = board.valid_moves()
        board_value = 0
        # pdb.set_trace()
        board_value += self.check_horizontal(board)
        board_value += self.check_vertical(board)
        board_value += self.check_diagonal_down(board)
        board_value += self.check_diagonal_up(board)
        board_value += self.check_middle(board)
        return board_value

    # Checking each row for possible 3 in a row or 4 in a row
    def check_horizontal(self, board):
        horizontal_value = 0
        for row in range(board.height):
            row_array = []
            for col in range(board.width):
                row_array.append(board.get_cell_value(row, col))
            for i in range(board.width - 3):
                window = row_array[i: i + 4]
                # If the window contains 4 player pieces
                # if window.count(self.id) == FOUR_IN_ROW:
                #     horizontal_value += WIN_VALUE
                # If window contains 3 player pieces and 1 empty piece
                # elif window.count(self.id) == THREE_IN_ROW and window.count(0) == 1:
                #     pdb.set_trace()
                    # horizontal_value += THREE_VALUE
                # elif window.count(self.id) == TWO_IN_ROW and window.count(0) == 2:
                #     horizontal_value += TWO_VALUE
                #
                # if window.count(self.opponent_id) == FOUR_IN_ROW:
                #     horizontal_value -= WIN_VALUE
                # elif window.count(self.opponent_id) == THREE_IN_ROW and window.count(0) == 1:
                #     horizontal_value -= THREE_VALUE
                # elif window.count(self.opponent_id) == TWO_IN_ROW and window.count(0) == 2:
                #     horizontal_value -= TWO_VALUE
                horizontal_value += self.get_window_value(window)
        return horizontal_value

    # Checking each column for possible 3 or 4 in column
    def check_vertical(self, board):
        vertical_value = 0
        for col in range(board.width):
            col_array = []
            # pdb.set_trace()
            for row in range(board.height):
                # Trying to get only the column value
                col_array.append(board.get_cell_value(row, col))
                # print(board.get_cell_value(row, col), end='')
            # print(*col_array)
            for i in range(board.height - 3):
                window = col_array[i: i + 4]
                # if window.count(self.id) == FOUR_IN_ROW:
                #     vertical_value += WIN_VALUE
                # elif window.count(self.id) == THREE_IN_ROW and window.count(0) == 1:
                #     vertical_value += THREE_VALUE
                # elif window.count(self.id) == TWO_IN_ROW and window.count(0) == 2:
                #     vertical_value += TWO_VALUE
                #
                # pdb.set_trace()
                # if window.count(self.opponent_id) == FOUR_IN_ROW:
                #     vertical_value -= WIN_VALUE
                # elif window.count(self.opponent_id) == THREE_IN_ROW and window.count(0) == 1:
                #     vertical_value -= THREE_VALUE
                # elif window.count(self.opponent_id) == TWO_IN_ROW and window.count(0) == 2:
                #     vertical_value -= TWO_VALUE
                vertical_value += self.get_window_value(window)
            # print()
        return vertical_value

    def check_diagonal_down(self, board):
        diagonal_value = 0
        for row in range(board.height - 3):
            for col in range(board.width - 3):
                window = []
                for i in range(WINDOW_LENGTH):
                    window.append(board.get_cell_value(row + i, col + i))
                # pdb.set_trace()
                # print(*window)
                # if window.count(self.id) == FOUR_IN_ROW:
                #     diagonal_value += WIN_VALUE
                # If window contains 3 player pieces and 1 empty piece
                # elif window.count(self.id) == THREE_IN_ROW and window.count(0) == 1:
                #     pdb.set_trace()
                    # diagonal_value += THREE_VALUE
                # elif window.count(self.id) == TWO_IN_ROW and window.count(0) == 2:
                #     diagonal_value += TWO_VALUE
                #
                # if window.count(self.opponent_id) == FOUR_IN_ROW:
                #     diagonal_value -= WIN_VALUE
                # elif window.count(self.opponent_id) == THREE_IN_ROW and window.count(0) == 1:
                #     diagonal_value -= THREE_VALUE
                # elif window.count(self.opponent_id) == TWO_IN_ROW and window.count(0) == 2:
                #     diagonal_value -= TWO_VALUE
                diagonal_value += self.get_window_value(window)
        return diagonal_value

    def check_diagonal_up(self, board):
        diagonal_value = 0
        for row in range(board.height - 1, board.height - 2, -1):
            for col in range(board.width - 3):
                window = []
                for i in range(WINDOW_LENGTH):
                    # pdb.set_trace()
                    window.append(board.get_cell_value(row - i, col + i))
        diagonal_value += self.get_window_value(window)
        return diagonal_value

    def check_middle(self, board):
        middle_value = 0
        board_copy = []
        for row in range(board.height):
            for col in range(board.width):
                board_copy.append(board.get_cell_value(row, col))

                if board.get_cell_value(row, col) == self.id:
                    if col == MIDDLE_COLUMN:
                        middle_value += 10
                    elif col == THIRD_COLUMN or col == FIFTH_COLUMN:
                        middle_value += 5
                    elif col == SECOND_COLUMN or col == SIXTH_COLUMN:
                        middle_value += 2
                    elif col == FIRST_COLUMN or col == SEVENTH_COLUMN:
                        middle_value += 1
        return middle_value

    def get_window_value(self, window):
        if self.id == 1:
            opponent_id = 2
        elif self.id == 2:
            opponent_id = 1

        window_value = 0
        if window.count(self.id) == FOUR_IN_ROW:
            window_value += WIN_VALUE
        # If window contains 3 player pieces and 1 empty piece
        elif window.count(self.id) == THREE_IN_ROW and window.count(0) == 1:
            window_value += THREE_VALUE
        elif window.count(self.id) == TWO_IN_ROW and window.count(0) == 2:
            window_value += TWO_VALUE

        if window.count(opponent_id) == FOUR_IN_ROW:
            # pdb.set_trace()
            window_value -= WIN_VALUE
        # elif window.count(opponent_id) == THREE_IN_ROW and window.count(0) == 1:
        #     window_value -= THREE_VALUE
        # elif window.count(opponent_id) == TWO_IN_ROW and window.count(0) == 2:
        #     window_value -= TWO_VALUE

        return window_value
