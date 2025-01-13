# Reverse Sliding Puzzle

## Overview
This is a sliding puzzle game where the player must arrange a shuffled grid of numbers in ascending order, leaving the empty tile (represented by `0`) in the bottom-right corner. The player can move tiles by sliding them into the empty space using the keyboard.

## [grid base](./grid_base.py)
### How to Play
1. The game initializes with a grid of numbers shuffled randomly.
2. The player uses the following keys to move tiles:
   - `w`: Move the empty tile **up**.
   - `s`: Move the empty tile **down**.
   - `a`: Move the empty tile **left**.
   - `d`: Move the empty tile **right**.
   - `SPACE`: Exit the game.
3. The goal is to arrange the tiles in ascending order, with the empty tile in the bottom-right corner.
4. The game ends with a congratulatory message upon successful completion.

### Code Explanation

#### 1. `getch()`
- **Purpose:** Captures a single character input from the user.
- **Platform-Specific:** Uses `msvcrt` on Windows and `termios`/`tty` on Unix-based systems.

#### 2. `initialize_board(size: int)`
- **Purpose:** Creates a shuffled grid of numbers of the specified size.
- **Input:**
  - `size`: The dimension of the grid (e.g., `5` for a 5x5 grid).
- **Output:** A two-dimensional list representing the shuffled grid.

#### 3. `print_board(board: list[list[int]])`
- **Purpose:** Displays the grid in the terminal with styled tiles.
- **Enhancement:** Highlights numbers for better readability; the empty tile is blank.

#### 4. `find_empty_tile(board: list[list[int]])`
- **Purpose:** Finds the position of the empty tile (`0`).
- **Output:** A tuple `(row, col)` representing the position of the empty tile.

#### 5. `is_valid_move(size: int, row: int, col: int)`
- **Purpose:** Checks if a move is valid within the grid boundaries.
- **Input:**
  - `size`: Dimension of the grid.
  - `row`, `col`: Target position.
- **Output:** `True` if the move is valid; `False` otherwise.

#### 6. `move_tile(board: list[list[int]], empty_pos: tuple[int, int], direction: str)`
- **Purpose:** Moves a tile into the empty space if the move is valid.
- **Input:**
  - `board`: Current state of the grid.
  - `empty_pos`: Position of the empty tile.
  - `direction`: Direction to move (`w`, `s`, `a`, `d`).
- **Output:** `True` if the move is successful; `False` otherwise.

#### 7. `is_solved(board: list[list[int]])`
- **Purpose:** Checks if the grid is arranged in ascending order with the empty tile at the bottom-right.
- **Output:** `True` if the puzzle is solved; `False` otherwise.

#### 8. `main()`
- **Purpose:** Main game loop that:
  1. Initializes the grid.
  2. Continuously displays the grid and accepts user input until the puzzle is solved.

### Algorithm
1. **Initialize Board:** Create a shuffled grid.
2. **Game Loop:**
   - Display the grid.
   - Capture user input and attempt to move a tile.
   - Check if the puzzle is solved after each move.
3. **End Game:** Display a congratulatory message when the puzzle is solved.

### User Requirements
1. **Python Installation:** Ensure Python 3.10+ is installed.
2. **Terminal:** Run the program in a terminal or command prompt.
3. **Platform-Specific Behavior:**
   - Windows: Ensure the `msvcrt` module is supported.
   - Unix-based systems: Use a compatible terminal that supports `termios` and `tty`.

### Steps to Run the Code
1. Open a terminal and navigate to the directory containing the file.
2. Run the program with the command:
   ```bash
   python ./grid_base.py
   ```

### Example Output
```plaintext
  12    5    8    7   10
   6    1   13   15    0
   9   14    4    2   11
   3   16   17   19   18
  20   21        23   22
Move the empty tile: w,s,a,d
```
