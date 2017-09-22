board = [[None]*15 for _ in range(15)]
"""
Board status is defined as
1 - my turn
0 - Opponent's turn 
"""

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

    if player in ["Goku", "goku"]: #basically our name
        try:
            board[x][y] = 1
        except IndexError:
            print "Bad move by the player. Can't insert at ", x, y

    else:
        try:
            board[x][y] = 0
        except IndexError:
            print "Bad move by the player. Can't insert at ", x, y

def get_board():
    return board

# insert_to_board("goku B 12")
