from connectfour.agents.computer_player import RandomAgent
import random
import pdb

THREE_IN_ROW = 3

FOUR_IN_ROW = 4

WIN_VALUE = 100000000000000


class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 1

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
        valid_moves = board.valid_moves()
        board_value = 0
        # If the game is over
        if board.terminal():
            if board.winner() == self.id:
                print("winner")
                for i in range(board.height):
                    for j in range(board.width):
                        print(board.get_cell_value(i, j), end=' ')
                    print()
                return WIN_VALUE
            elif board.winner() != self.id and board.winner() != 0:
                print("loser")
                for i in range(board.height):
                    for j in range(board.width):
                        print(board.get_cell_value(i, j), end=' ')
                    print()
                return -1000000000000000
            else:
                # print("Draw")
                print("loser")
                for i in range(board.height):
                    for j in range(board.width):
                        print(board.get_cell_value(i, j), end=' ')
                    print()
                return -1000000000000000
                # return 0
        # If game is still in progress
        else:
            # pdb.set_trace()
            for row in range(board.height):
                row_array = []
                for col in range(board.width):
                    row_array.append(board.get_cell_value(row, col))
                for i in range(board.width - 3):
                    window = row_array[i: i+4]
                    # If the window contains 4 player pieces
                    if window.count(self.id) == FOUR_IN_ROW:
                        board_value += WIN_VALUE
                    if window.count(self.id) == THREE_IN_ROW and window.count(0) == 1:
                        # pdb.set_trace()
                        board_value += 10
            print(board_value)
            return board_value

