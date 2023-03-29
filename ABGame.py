import sys
from MiniMaxOpening import GenerateMovesMidEndBlack, GenerateMovesMidEnd, StaticEstimateMidEnd, state

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

        def ABgame(depth, board, a, b, label):
            exit = state()
            entry = state()

            if label == 0:
                move_list = GenerateMovesMidEndBlack(board)
            else:
                move_list = GenerateMovesMidEnd(board)

            if depth == 0: 
                counter_final = StaticEstimateMidEnd(board)
                exit = state(counter_final, exit.counter + 1, board)
                return exit
            

            for move in move_list:
                if a >= b: 
                    break

                if label == 0: 
                    entry = ABgame(depth-1, move, a, b, 1)
                    if entry.estimate < b:
                        b = entry.estimate
                        exit.board = move
                
                    exit.counter += entry.counter

                else:
                    entry = ABgame(depth - 1, move, a, b, 0)
                    if entry.estimate > a:
                        a = entry.estimate
                        exit.board = move

                    exit.counter += entry.counter
            
            if label == 1:
                exit.estimate = a
            else:
                exit.estimate = b
                
            return exit

        def run():
            result = ABgame(self.depth, self.curr_board, MIN, MAX, 1)
            print('Board Position: ', result.board)
            print('Positions Evaluated by Static Estimaton:', result.counter)
            print('AB Estimate:', result.estimate)
            write_result(result.board)

        run()


if __name__ == '__main__':
    board = ''
    with open(sys.argv[1], 'r') as f: 
        for line in f:
            board = line

    depth = int(sys.argv[3])
    Solution(board, depth)