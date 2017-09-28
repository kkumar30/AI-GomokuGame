import Eval

board = [[None]*15 for _ in range(15)]
globaldepth = 0
"""
Board status is defined as
1 - my turn
0 - Opponent's turn 
"""

"""
Team Name defined as below - Goku
"""
myteamname = ["Goku, goku"]


def refresh():
    global board
    board = [[None] * 15 for _ in range(15)]

def print_board():
    for i in board:
        print i,"\n"

def insert_to_board(movestring):
    player, x, y = movestring.split(" ")
    print "Inserting at .. ", x, y
    x = int(ord(x.lower()) - 96) - 1
    y = int(y) - 1
    # print x, y

    if player in myteamname: #basically our name
        try:
            board[x][y] = 1
        except IndexError:
            print "Bad move by the player. Can't insert at ", x, y

    else:
        try:
            board[x][y] = 0
        except IndexError:
            print "Bad move by the player. Can't insert at ", x, y

"""
Board getter
"""
def get_board():
    return board

# insert_to_board("goku B 12")


"""
Alpha Beta Pruning
"""

def alpha_beta_search(board):
    best_row = -1
    best_col = -1
    best_eval = -(float("inf"))

    for x in range(0,15):
        for y in range(0,15):
            if board[x][y] == None and check_neighbor(board, x, y): #only checks if the element is inserted near a board piece
                board[x][y] = 1
                v = max_value(board, -(float("inf")), (float("inf")), 2)
                print v
                board[x][y] = None

                if v > best_eval:
                    best_eval = v
                    best_row = x
                    best_col = y
            #How to return the next filled board state??
    return best_row, best_col


"""
**********************************Max Value calculation*********************************
function MAX-VALUE(state,alpha, b) returns a utility value

"""

def max_value(state, alpha, beta, depth):
    local_depth = 0
    print "Depth =", depth
    global globaldepth
    if globaldepth == 2:
        return evaluation(state)
    if terminal(state) == None:
        return utility(state)
    v = -float("inf")

    for x in range(0,15):
        for y in range(0,15):
            if state[x][y] == None and check_neighbor(board, x, y): #only checks if the element is inserted near a board piece
                state[x][y] = 1
                v = max(v, min_value(state, alpha, beta, depth-1))
                state[x][y] = None
            if v >= beta:
                return v
            alpha = max(alpha, v)
    local_depth += 1
    globaldepth += 1
    return v

"""
************************************Min Value calculation***********************************
function MIN-VALUE(state,)
"""

def min_value(state, alpha, beta, depth):

    global globaldepth
    if globaldepth == 2:
        return evaluation(state)
    if terminal(state) == None:
        return utility(state)
    v = float("inf")

    for x in range(0,15):
        for y in range(0,15):
            if state[x][y] == None and check_neighbor(board, x, y):
                state[x][y] = 0
                v = min(v, max_value(state, alpha, beta, depth))
                state[x][y] = None
            if v <= alpha:
                return v
            beta = min(beta, v)
        globaldepth += 1
    return v


def utility(state):
    return 1

def evaluation(state):
    pass

# def terminal(state):
#     pass
    #check neighbouring all 5 win/loss

"""
Helper function for check_neighbors
"""
def safe_get(arry, x, y, default):
    try:
        return arry[x][y]
    except IndexError:
        return default

"""
Checks for neighbours in the board cell for a given position
"""
def check_neighbor(board, x, y):
    flag = any(
        [
            safe_get(board, x, y + 1, None) != None,
            safe_get(board, x, y - 1, None) != None,
            safe_get(board, x + 1, y, None) != None,
            safe_get(board, x - 1, y, None) != None,
            safe_get(board, x - 1, y + 1, None) != None,
            safe_get(board, x + 1, y + 1, None) != None,
            safe_get(board, x - 1, y - 1, None) != None,
            safe_get(board, x + 1, y - 1, None) != None
        ]
    )

    return flag


def terminal(board):
    if Eval.utilGen2(board) >= 10000 or Eval.utilGen2(board) <= -10000:
        return True
    dval = True

    for i in board:
        for j in i:
            if(j == None):
                dval = False

    return dval

