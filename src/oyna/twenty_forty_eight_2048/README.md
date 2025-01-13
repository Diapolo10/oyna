# 2048

## Overview:
The 2048 game is a popular puzzle game where players combine tiles with the same value to reach the tile with the number 2048. In this console-based version, you control the game using keyboard inputs to move the tiles on a grid, merging them to achieve higher values. The game ends when no more moves can be made or when the tile with the value of 2048 is reached.

## [grid base](./grid_base.py)

### How to Play:
1. **Objective**: The goal of the game is to combine tiles of the same value to form larger tiles. The game ends when the 2048 tile is reached or when there are no possible moves left.
2. **Controls**:
   - **w**: Move tiles up.
   - **s**: Move tiles down.
   - **a**: Move tiles left.
   - **d**: Move tiles right.
   - **Space**: Quit the game.
3. **Gameplay**:
   - Tiles can move in any of the four directions: up, down, left, or right.
   - When two tiles of the same value collide, they merge into one with double the value.
   - After every move, a new tile with the value 2 will appear in an empty cell.
   - The game continues until either the 2048 tile is formed, or no more moves can be made.

### How to Install and Run:
1. **Requirements**:
   - Python 3.x is required to run this game.
   - The game uses the `msvcrt` module on Windows for capturing key presses, and the `termios` module for Unix-based systems (Linux/macOS).

2. **Installation**:
   - Download the Python script file to your computer.
   - Ensure that Python 3.x is installed on your system.

3. **Execution**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the Python script is saved.
   - Run the script by typing:
     ```bash
     python3 grid_base.py
     ```
   - The game will start, and you can begin playing by using the arrow keys (W, A, S, D) or the spacebar to quit.

### Algorithm and Implementation:

The code for the game consists of several key components:
1. **Cell Class**:
   - Each cell on the game board is represented by the `Cell` class. A cell can either be empty (blocked), contain a value, or serve as a wall. The `Cell` class manages its value and neighbors (up, down, left, right).

2. **Board Class**:
   - The `Board` class represents the game grid. It initializes the grid, sets up walls around the board, and manages valuable cells where tiles will appear.
   - The board also includes methods to handle player input (via the `take` method) and to move tiles (via the `move` method). The game state is updated after each move.

3. **Game Logic**:
   - The game runs in a loop, accepting player inputs (using `getch()`), updating the game board, and displaying the updated board after each move.
   - A random tile with the value of 2 is placed after each move.
   - The game ends when there are no possible moves or when a tile reaches the value 2048.

4. **Helper Functions**:
   - `rgb_bg()`: Changes the background color of the terminal output based on tile values.
   - `rgb()`: Changes the text color of the terminal output.
   - `reset()`: Resets the color formatting in the terminal after each tile display.

### Code Walkthrough:
- **Initialization**:
   - The `Board` is initialized with a 4x4 grid (adjustable size) and walls around the edges.
   - The initial value of `2` is placed in some random cells.

- **Gameplay**:
   - The game listens for user input and moves the tiles accordingly.
   - The tiles can merge if they have the same value and are adjacent to each other in the direction the player moves.
   - A new tile is randomly placed in an empty cell after each move.

- **End Condition**:
   - The game ends when the 2048 tile is formed or when there are no more moves possible.

### Key Concepts and Functions:
1. **getch()**:
   - This function captures user input (single character) in a way that works across different operating systems (Windows and Unix-based).

2. **State Enum**:
   - The `State` enum defines various states for the cells, such as `BLOCK` (empty), `WALL` (boundary of the grid), `CONTINUE` (game in progress), and `END` (game over).

3. **Action Enum**:
   - The `Action` enum defines the available player actions, such as moving in various directions (`MOVE_UP`, `MOVE_DOWN`, etc.) or exiting the game.

4. **Cell Value Display**:
   - Each cell in the game grid can display its value with different colors based on the tile's value. This is done using ANSI escape codes.

### Conclusion:
This console-based 2048 game is a simple yet fun implementation of the popular puzzle game. By following the instructions above, you can easily run and play the game in your terminal. The game's logic involves moving and merging tiles, with a random tile appearing after each move, and the game ends either when you reach the 2048 tile or when no more moves are possible.
