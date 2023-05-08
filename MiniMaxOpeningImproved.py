import sys 
from MiniMaxOpening import GenerateMovesOpeningBlack, GenerateMovesOpening, StaticEstimateOpeningImproved, state

MIN = -9000000000000
MAX = 9000000000000

class Solution:
    def __init__(self, board = '', depth = 0):
        self.curr_board = board
        self.depth = depth

        def write_result(board):
            with open(sys.argv[2], 'w') as f:
                for line in board: 
                    f.write(line)

        def minmaxopening(depth, board, label):
            exit = state()
            entry = state()

            if label == 0:
                move_list = GenerateMovesOpeningBlack(board)
                exit.estimate = MAX
            else:
                move_list = GenerateMovesOpening(board)
                exit.estimate = MIN

            if depth == 0: 
                counter_final = StaticEstimateOpeningImproved(board)
                exit = state(counter_final, exit.counter + 1, board)
                return exit
            

            for move in move_list:
                if label == 0: 
                    entry = minmaxopening(depth-1, move, 1)
                    if entry.estimate < exit.estimate:
                        exit.board = move
                        exit.estimate = entry.estimate
                    
                    exit.counter += entry.counter

                else:
                    entry = minmaxopening(depth - 1, move, 0)
                    if entry.estimate > exit.estimate:
                        exit.board = move
                        exit.estimate = entry.estimate
                    
                    exit.counter += entry.counter
                
            return exit

        def run():
            result = minmaxopening(self.depth, self.curr_board, 1)
            print('Board Position: ', result.board)
            print('Positions Evaluated by Static Estimation:', result.counter)
            print('MINIMAX Estimate:', result.estimate)
            write_result(result.board)

        run()


if __name__ == '__main__':
    board = ''
    with open(sys.argv[1], 'r') as f: 
        for line in f:
            board = line

    depth = int(sys.argv[3])
    Solution(board, depth)