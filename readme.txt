Improved Version of Gomuku Game that wins against our previous version.

1. Members:
Kushagra Kumar
Maximillian Hoerhold


2. How to run:
To run the program please go to inside the directory of the program and then run the following command-

python goku.py

[Our team Name is "Goku" or "goku"]

This will update the file in the referee move_file. 


3. Utility function:
The utility function of our program finds the distance of the longest chain of each row and uses this value to determine the utility of the board state.  In order to do this, the utility of a row, column, or diagonal, is set to be 10 to the power of the row's longest chain which is not blocked on both ends.  This way lengthening the longest possible chain gives the greatest possible value.  this value is positive if the chain is your own, and negative if an opponent's.  The utility of the board is then the sum of the utility of the rows, columns, and diagonals  the function also does not count chains that are surrounded by opposing pieces as those cannot be lengthened.


4. Evaluation function:
Our program uses an evaluation function which selects nodes in which the player is placing a piece near an existing piece on the board.  It does this by checking the adjacent positions of pieces to find the best nodes to expand.  This is because the best move is usually to lengthen your own chain or block an opponent's chain.  This significantly reduces the number of nodes expanded.


5. The heuristics and/or strategies that you employed to decide how to expand (pieces of) the minimax tree without exceeding your time limit:

We set up a depth limit such that we don't expand more than a certain depth so that we get a move within the time limit (10 seconds). We also worked on choosing the node of the tree (during expansion) in such a manner so that we only look for cases by inserting the piece near to an existing piece on the board. We will lose a lot of computational time if we don't choose the relevant next tree node. We then applied the minimax algorithm along with Alpha beta pruning to compute our best possible move.


6. Results:
To test the referee communication part of the program, we made dummy files and tested our 
functions along with the helper function. 

The main strengths of our program are that it uses a heuristic closely related to the game's win condition and returns a move in the time limit.  The main weakness of our program is that the heuristic we use is fairly time consuming to calculate.


7. A discussion of why the evaluation function and heuristic(s) you picked are good choices:

The heuristic we used was a good choice because it is based mainly on the longest chains of pieces existing on the board.  This is because the longer a player�s longest chain is, the closer the player is to winning.  The function also checks that a chain has at least one end not blocked by an opponent, because if it is blocked on both ends it cannot be lengthened to get closer to the win condition.  The evaluation function we used selects nodes which insert pieces next to existing pieces on the board.  This is because the optimal move is almost always adjacent to a friendly or opponent�s piece because this will either lengthen your own chain or block an opponent's chain.  It is not worth the time to expand all other nodes in the tree.
