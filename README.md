# Neutreeko_A.I._2021

Development of the Neutreeko board game with an A.I. engine based on the Minimax method

Python libraries required:
 - numpy
 - game2dboard
 - easygui

The following libraries are also needed, but usually come already installed: - copy
									     - random
									     - time
									     - math

In the same directory of the Neutreeko_AI.py file, there should be a \img folder, with the pieces images!


After installing the libaries and \img folder, the python code can be compiled and runned. The GUI will appear, starting the game!

The GUI presents a main menu with the game rules and a play button. Black moves first.
After that it allows the user to choose the size of the square board. Each player has 3 pieces.

Then the game mode can be selected. (Pressing the right arrow key gives a hint. Pressing the left arrow key shows the history of moves in the terminal.)

  - In Human Vs Human, the game is played by selecting the piece you want to move. The possible moves appear. Click on the square you want to move to.

  - In Human Vs Computer, the human goes first. The first 2 levels the engine plays imedeatelly. The last most difficult level (Depth=4) the A.I. takes30 sec to 1 min  to calculate.

  - In Computer Vs Computer, after starting, the GUI moves for itself. The GUI can break if clicked unfortunatelly (internal problem with the library). After the final  message the board doesn't close on purpose, since the user may want to see the final board state or the history of moves, pressing the left arrow key.


If you want to move to a different game mode or board size, close the game window and recompile the program, starting from the begining.