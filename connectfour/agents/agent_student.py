from connectfour.agents.computer_player import RandomAgent
import random


def check_three_rows(board):
    three_in_row = 3
    for row in board:
        same_count = 1
        curr = row[0]
        for i in range(1, board.width):
            if row[i] == curr:
                same_count += 1
                if same_count == three_in_row and curr != 0:
                    return curr
            else:
                same_count = 1
                curr = row[i]
    return 0


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
        board_value = 0
        # how many three in a row does this player have
        three_in_row = check_three_rows(board)
        two_in_row = 0
        disjointed_three = 0
        disJointed_two = 0

        if board.winner(board) == self.id:
            return 1
        elif board.winner(board) != self.id and board.winner(board) != 0:
            return -1
        else:
            return random.uniform(0, 1)
            # return board_value

    '''
    def getThreesInRow(self, board):
        three_in_row = 0
        for row in range(board.width):
            for col in range(board.height):
    '''
