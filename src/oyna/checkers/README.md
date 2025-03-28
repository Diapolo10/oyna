# Checkers

## Overview:
Checkers is a classic strategy board game played between two players. In this console-based version, you can play against a simple AI. The objective is to capture all of your opponent's pieces or block them so they cannot make a move.

## [grid base](./grid_base.py)

### How to Play:
1. **Objective**: The goal of the game is to capture all of the opponent's pieces or block them from making any valid moves.
2. **Controls**:
   - **w**: Move the cursor up.
   - **s**: Move the cursor down.
   - **a**: Move the cursor left.
   - **d**: Move the cursor right.
   - **e**: Select a piece or place it in a valid position.
   - **Space**: Quit the game.
3. **Gameplay**:
   - Players take turns moving their pieces diagonally forward.
   - A piece can capture an opponent's piece by jumping over it to an empty square.
   - The AI will make its move after the player completes theirs.
   - Pieces cannot move backward unless they are promoted to kings (not implemented in this version).

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
   - The game will start, and you can begin playing by using the controls described above.

### Algorithm and Implementation:

The code for the game consists of several key components:
1. **Emoji Enum**:
   - Represents the different types of pieces on the board:
     - `EMPTY`: An empty square.
     - `PLAYER`: The player's piece.
     - `COMPUTER`: The AI's piece.

2. **Board Class**:
   - The `Board` class represents the game grid. It initializes the grid, sets up the pieces, and manages the game state.
   - The board includes methods to handle player input, validate moves, and execute moves for both the player and the AI.

3. **Game Logic**:
   - The game runs in a loop, accepting player inputs (using `getch()`), updating the game board, and displaying the updated board after each move.
   - The AI makes its move immediately after the player completes theirs.
   - The game ends when one player has no valid moves left.

4. **Helper Functions**:
   - `getch()`: Captures user input (single character) in a way that works across different operating systems (Windows and Unix-based).
   - `print_board()`: Displays the game board in the terminal, highlighting the selected piece and valid moves.

### Code Walkthrough:
- **Initialization**:
   - The `Board` is initialized with an 8x8 grid and pieces placed in their starting positions.
   - The player's pieces are placed on the bottom three rows, and the AI's pieces are placed on the top three rows.

- **Gameplay**:
   - The player selects a piece using the `e` key and moves it to a valid position.
   - The AI calculates its move based on simple logic, prioritizing capturing the player's pieces.

- **End Condition**:
   - The game ends when one player has no valid moves left or all their pieces are captured.

### Key Concepts and Functions:
1. **get_valid_moves_for_piece()**:
   - Calculates all valid moves for a given piece, ensuring that backward moves are not allowed for regular pieces.

2. **make_move()**:
   - Executes a move, updating the board and handling captures.

3. **computer_move()**:
   - Implements simple AI logic to make a move, prioritizing capturing the player's pieces.

4. **print_board()**:
   - Displays the game board in the terminal, highlighting the selected piece and valid moves.

### OutPut:
```
🔹⚫️🔹⚫️🔹⚫️🔹⚫️
⚫️🔹⚫️🔹⚫️🔹⚫️🔹
🔹⚫️🔹⚫️🔹⚫️🔹⚫️
🔹🔹🔹🔹🔹🔹🔹🔹
🔹🔹🔹🔹🔹🔹🔹🔹
🔴🔹🔴🔹🔴🔹🔴🔹
🔹🔴🔹🔴🔹🔴🔹🔴
🔴🔹🔴🔹🔴🔹🔴🔹
```


### Conclusion:
This console-based Checkers game provides a simple yet engaging way to play against an AI. By following the instructions above, you can easily run and play the game in your terminal. The game's logic ensures fair play, and the AI provides a basic challenge for players.
