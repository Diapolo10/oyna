# Othello Game - README


## Overview

This is a console-based implementation of a classic Othello (Reversi) game. The game allows a player to compete against the computer on an 8x8 board. The player can move around the board using the keyboard (WASD keys), place their pieces, and watch as the computer makes its moves. The game continues until neither player can make a valid move. The game is written in Python and uses basic console input/output for interaction.

## [grid base](./grid_base.py)
### How to Play

1. **Objective**: The objective of Othello is to have the majority of your colored pieces on the board at the end of the game. You place pieces on the board in such a way that you "flip" your opponent's pieces. The game alternates turns between the player and the computer.

2. **Board Setup**: The game starts with a 8x8 grid, where the center of the board has four pieces: two computer pieces (⚫️) and two player pieces (⚪️).

3. **Player Moves**: The player can move their piece by pressing one of the following keys:
   - `w`: Move up
   - `a`: Move left
   - `s`: Move down
   - `d`: Move right
   - `e`: Skip turn (if no valid moves are available)
   - `Space`: Exit the game

4. **Valid Moves**: A valid move occurs when a piece is placed on an empty spot and at least one of the opponent's pieces will be flipped by the move. The directions in which pieces can be flipped are horizontal, vertical, and diagonal.

5. **Computer Moves**: The computer makes its move after the player. It picks a random valid move from the available options.

6. **Game End**: The game ends when neither the player nor the computer can make a valid move. The winner is determined by the number of pieces on the board.

### Features

- **Interactive Console Game**: You control the player piece using the WASD keys.
- **Valid Move Checking**: The game checks if a move is valid according to Othello rules.
- **Computer Opponent**: The computer makes moves randomly from available options.
- **Board Display**: The board is printed after each move, with different colors for the player, computer, valid moves, and empty spots.
- **Turn-Based**: The game alternates between the player's and computer's turns.

### Requirements

- **Python**: Python 3.x (The game should work on most versions of Python 3).
- **Libraries**:  Only Python standard libraries

### Installation

To run the game, simply clone or download the repository and execute the Python file. Ensure you have Python 3 installed on your system.

```bash
python3 ./grid_base.py
```

### Algorithm

1. **Board Initialization**:
   - The board is initialized with a size of 8x8, and four central pieces are placed: two for the player and two for the computer.

2. **Player Movement**:
   - The player can move using the WASD keys. The `getch()` function handles keypresses and determines the movement direction.
   - Each move is validated by checking surrounding cells to see if an opponent's piece will be flipped.

3. **Computer Movement**:
   - The computer randomly selects from valid moves after the player's turn. The `computer_move()` function picks a random valid move and flips the opponent's pieces.

4. **Flipping Pieces**:
   - For each move, the `make_move()` function flips the opponent's pieces along the valid direction(s) if applicable.

5. **Game State**:
   - After each turn, the board is displayed with the updated positions.
   - If no valid moves are available, the player can skip their turn by pressing 'e'.
   - The game ends when neither player can make a valid move. The score (number of player and computer pieces) is displayed.

### Example of Board Display

Here's how the game board might look at the start:

```
🔹🔹🔹🔹🔹🔹🔹🔹
🔹🔹🔹🔹🔹🔹🔹🔹
🔹🔹🔹🔹🔹🔹🔹🔹
🔹🔹🔹⚫️⚪️🔹🔹🔹
🔹🔹🔹⚪️⚫️🔹🔹🔹
🔹🔹🔹🔹🔹🔹🔹🔹
🔹🔹🔹🔹🔹🔹🔹🔹
🔹🔹🔹🔹🔹🔹🔹🔹
```

### Troubleshooting

- **No input after pressing keys**: If the game is not responding to keypresses, ensure that the script is running in a terminal that supports the `msvcrt` (Windows) or `termios` (Linux/Mac) libraries for non-blocking input.

- **Invalid characters for input**: Make sure you are pressing one of the specified keys (`w`, `a`, `s`, `d`, `e`, Space) to control the game.
