import sys, os
import time
import Board

safety_count = 0
groupname = "goku"
mygroupname_file = groupname + ".go"
# file_groupname = "referee.py" #Comment this out
print mygroupname_file

#For getting into the referee directory
referee_files = os.listdir("gomoku")
print referee_files
#END GAME FILE checking initialization
end_game_file = "end_game"
# end_game_file = "referee" #Comment this out
path = "gomuku"
starting_time1 = time.time()
##Function Calls
#Here is where we need to perform minimax function
def generate_solution(move, starting_time):
    # global starting_time1

    if len(move) > 1:
        x, y = Board.alpha_beta_search(Board.board, starting_time, False)
    else:
        x, y = Board.alpha_beta_search(Board.board, starting_time, True)
    print "After alpha beta ", x,y
    x_axis = chr(x + 65)
    y_axis = int(y) + 1
    final_move = str(x_axis) + " " + str(y_axis)
    return final_move


    # return groupname + " A 10"
#Fetch the move from the file
def fetch_opponent_move():
    with open("gomoku/move_file") as file:
        return file.read()

#Write our move to the file
def send_move(move):
    with open("gomoku/move_file", "w") as file:
        file.write(groupname + " " + move)


while True: # safety_count <3:

    while mygroupname_file not in os.listdir("gomoku"):
        continue

    starting_time = time.time()

    isEndGameExist = [True for file in referee_files if end_game_file in file]

    if True not in isEndGameExist: #means end_game file not present, so can call for the turn for minimax calculator
        print "No end game File found! Continuing my turn..."

        #Get the opponent's move
        opponent_move = fetch_opponent_move()
        print "Opponent move = ", opponent_move

        #Insert to board with the opponents move
        Board.insert_to_board(opponent_move)

        #Generate my move
        my_move = generate_solution(opponent_move, starting_time)
        print "My move = ", my_move

        #Write move to Referee's move_file
        send_move(my_move)

        safety_count +=1
        time.sleep(0.18) #Wait for 100 ms
    else:
        #end_game file is present
        print "Game Over!"
        break


## To test the Functionality export of the board
# print "Printing the board"
# Board.print_board()
# print "After refresh, \n"
# Board.refresh()
# Board.print_board()
# print "Adding command goku A 5"
# Board.insert_to_board("Goku A 5")
Board.print_board()