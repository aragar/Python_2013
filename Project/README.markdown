Implementation of the game [Reversi](http://en.wikipedia.org/wiki/Reversi) on Python3.3

The project contains the following AI techniques:
* Trivial AI - it plays the first possible move;
* Greedy AI - it plays the move which takes most of the opponent's pieces;
* [Alpha-Beta prunning](http://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) - it deepens four levels;
All of them are in the ''reversi_ai'' directory.

The board implementation is in the ''reversi_board'' directory. The board is made to be used like a two-dimensional array with no additional methods for getting or setting a piece, i.e. board[x][y] will place a piece at position (x, y). Additionally, some methods are provided returning the possible moves, the pieces to be flipped, or whether the player can move. The board has a console representation with no additional GUI.

Basic implementation of human and computer interaction is placed in the reversi_player directory. 

The game itself is controlled form the reversi_game.py file, placed in the reversi_play directory.