import copy
import sys 

MIN = -9000000000000
MAX = 9000000000000

def GenerateAdd(board):
    L = list() 
    for location, piece in enumerate(board):
        if piece == 'x':
            b = copy.deepcopy(board)
            b = list(b)
            b[location] = 'W'
            b = "".join(b)
            if closeMill(location, b):
                L = GenerateRemove(b, L)
            else: 
                L.append(b)

    return L



def GenerateMove(board):
    L = list()
    for location, piece in enumerate(board):
        if piece == 'W':
            n = neighbors(location)
            for j in n:
                if board[j] == 'x':
                    b = copy.deepcopy(board)
                    b = list(b)
                    b[location] = 'x'
                    b[j] = 'W'
                    b = "".join(b)
                    if closeMill(j, b):
                        L = GenerateRemove(b, L)
                    else: 
                        L.append(b)
    
    return L

def GenerateRemove(board, L):
    flag = True
    for location, piece in enumerate(board):
        if piece == 'B':
            if not closeMill(location, board):
                flag = False
                b = copy.deepcopy(board)
                b = list(b)
                b[location] = 'x'
                b = "".join(b)
                L.append(b)
    
    if flag: 
        L.append(board)

    return L


def GenerateHopping(board):
    L = list()
    for i, p in enumerate(board):
        if p == 'W':
            for j, piece in enumerate(board):
                if piece == 'x':
                    b = copy.deepcopy(board)
                    b = list(b)
                    b[i] = 'x'
                    b[j] = 'W'
                    b = "".join(b)
                    if closeMill(j, b):
                        L = GenerateRemove(b, L)
                    else:
                        L.append(b)
    
    return L

def neighbors(position):
    match position:
        case 0:
            return [1, 3, 19]
        case 1:
            return [0, 2, 4]
        case 2:
            return [1, 5, 12]
        case 3:
            return [0, 4, 6, 8]
        case 4:
            return [1, 3, 5]
        case 5:
            return [2, 4, 7, 11]
        case 6:
            return [3, 7, 9]
        case 7:
            return [5, 6, 10]
        case 8:
            return [3, 9, 16]
        case 9:
            return [6, 8, 13]
        case 10:
            return [7, 11, 13]
        case 11:
            return [5, 10, 12, 18]
        case 12:
            return [2, 11, 21]
        case 13:
            return [9, 14, 16]
        case 14:
            return [13, 15, 17]
        case 15:
            return [10, 14, 18]
        case 16:
            return [8, 13, 17, 19]
        case 17:
            return [14, 16, 18, 20]
        case 18:
            return [11, 13, 17, 21]
        case 19:
            return [0, 16, 20]
        case 20:
            return [17, 19, 21]
        case 21:
            return [12, 18, 20]
        

def closeMill(loc, board):
    c = board[loc]
    if c == 'x':
        return False
    
    match loc:
        case 0:
            if (board[1] == c and board[2] == c) or (board[3] == c and board[6] == c):
                return True
        case 1:
            if (board[0] == c and board[2] == c):
                return True
        case 2:
            if (board[0] == c and board[1] == c) or (board[5] == c and board[7] == c) or (board[12] == c and board[21] == c):
                return True
        case 3:
            if (board[0] == c and board[6] == c) or (board[4] == c and board[5] == c) or (board[8] == c and board[16] == c):
                return True
        case 4:
            if (board[3] == c and board[5] == c):
                return True
        case 5:
            if (board[3] == c and board[4] == c) or (board[2] == c and board[7] == c) or (board[11] == c and board[18] == c):
                return True
        case 6:
            if (board[0] == c and board[3] == c) or (board[9] == c and board[13] == c):
                return True
        case 7:
            if (board[2] == c and board[5] == c) or (board[10] == c and board[15] == c):
                return True
        case 8:
            if (board[3] == c and board[16] == c):
                return True
        case 9:
            if (board[6] == c and board[13] == c):
                return True
        case 10:
            if (board[11] == c and board[12] == c) or (board[7] == c and board[15] == c):
                return True
        case 11:
            if (board[10] == c and board[12] == c) or (board[5] == c and board[18] == c):
                return True
        case 12:
            if (board[10] == c and board[11] == c) or (board[2] == c and board[21] == c):
                return True
        case 13:
            if (board[14] == c and board[15] == c) or (board[6] == c and board[9] == c) or (board[16] == c and board[19] == c):
                return True
        case 14:
            if (board[13] == c and board[15] == c) or (board[16] == c and board[20] == c):
                return True
        case 15:
            if (board[13] == c and board[14] == c) or (board[7] == c and board[10] == c) or (board[18] == c and board[21] == c):
                return True
        case 16:
            if (board[17] == c and board[18] == c) or (board[13] == c and board[19] == c) or (board[3] == c and board[8] == c):
                return True
        case 17:
            if (board[16] == c and board[18] == c) or (board[14] == c and board[20] == c):
                return True
        case 18:
            if (board[15] == c and board[21] == c) or (board[16] == c and board[17] == c) or (board[5] == c and board[11] == c):
                return True
        case 19:
            if (board[20] == c and board[21] == c) or (board[13] == c and board[16] == c):
                return True
        case 20:
            if (board[19] == c and board[21] == c) or (board[14] == c and board[16] == c):
                return True
        case 21:
            if (board[2] == c and board[12] == c) or (board[19] == c and board[20] == c):
                return True

    return False

def reverse(board):
    board = board.replace('W', 'k')
    board = board.replace('B','W')
    board = board.replace('k', 'B')

    return board

def StaticEstimateOpening(board):
    num_white = board.count('W')
    num_black = board.count('B')

    return num_white - num_black

def StaticEstimateOpeningImproved(board):
    num_white = board.count('W')
    num_black = board.count('B')

    white_mills = 0
    black_mills = 0
    for loc, piece in enumerate(board):
        if piece == 'W' and closeMill(loc, board):
            white_mills += 1
        if piece == 'B' and closeMill(loc, board):
            black_mills += 1 

    return num_white + (3*(white_mills - black_mills)) - num_black


def StaticEstimateMidEnd(board):
    num_white = board.count('W')
    num_black = board.count('B')

    possible_black_moves = GenerateMovesMidEndBlack(board)
    num_black_moves = len(possible_black_moves)

    if num_black <= 2:
        return 10000
    elif num_white <= 2:
        return -10000
    elif num_black_moves == 0:
        return 10000
    else:
        return 1000*(num_white - num_black) - num_black_moves
    
def StaticEstimateMidEndImproved(board):
    white_mills = 0
    black_mills = 0
    for loc, piece in enumerate(board):
        if piece == 'W' and closeMill(loc, board):
            white_mills += 1
        if piece == 'B' and closeMill(loc, board):
            black_mills += 1 

    num_white = board.count('W')
    num_black = board.count('B')

    possible_black_moves = GenerateMovesMidEndBlack(board)
    num_black_moves = len(possible_black_moves)

    if num_black <= 2:
        return 10000
    elif num_white <= 2:
        return -10000
    elif num_black_moves == 0:
        return 10000
    else:
        return 1000*(num_white - num_black + white_mills) - num_black_moves
    
def GenerateMovesOpeningBlack(board):
    tmp_board = reverse(board)

    L = GenerateAdd(tmp_board)
    L = [reverse(brd) for brd in L]
    return L

def GenerateMovesMidEndBlack(board):
    tmp_board = reverse(board)
    L = GenerateMovesMidEnd(tmp_board)
    L = [reverse(brd) for brd in L]
    return L


def GenerateMovesOpening(board):
    return GenerateAdd(board)

def GenerateMovesMidEnd(board):
    if board.count('W') == 3:
        return GenerateHopping(board)
    else:
        return GenerateMove(board)


class state:
    def __init__(self, estimate = 0, counter = 0, board = ''):
        self.estimate = estimate
        self.counter = counter
        self.board = board

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
                counter_final = StaticEstimateOpening(board)
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

    
    
