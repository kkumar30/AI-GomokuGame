import sys, os
import time


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

##Function Calls
#Here is where we need to perform minimax function
def generate_solution(move):
    return groupname + " A 10"
#Fetch the move from the file
def fetch_opponent_move(directory):
    with open("gomoku/move_file.txt") as file:
        return file.read()
#Write our move to the file
def send_move(move):
    with open("gomoku/move_file.txt", "w") as file:
        file.write(move)


while mygroupname_file in os.listdir("gomoku"):
    isEndGameExist = [True for file in referee_files if end_game_file in file]
    if True not in isEndGameExist: #means end_game file not present, so can call for the turn for minimax calculator
        print "No end game File found! Continuing my turn..."
        opponent_move = fetch_opponent_move(referee_files)
        print "Opponent move = ", opponent_move
        my_move = generate_solution(opponent_move)
        print "My move = ", my_move
        send_move(my_move)
        safety_count +=1
        time.sleep(0.1) #Wait for 100 ms


