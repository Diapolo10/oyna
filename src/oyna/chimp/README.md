# Chimp

## Overview
This is a simple grid-based board game where the player navigates through a board to collect numbered tiles in ascending order. The game is interactive and text-based, providing a unique and challenging experience.
## [grid base](./grid_base.py)

### How to Play
1. **Objective**: Collect the numbers on the board in ascending order (1, 2, 3, ...) to win the game.
2. **Movement Controls**:
   - `w`: Move up
   - `a`: Move left
   - `s`: Move down
   - `d`: Move right
   - `e`: Collect the number at the current position
   - `space`: Exit the game
3. **Winning Condition**: Collect all the numbers in the correct order to win.
4. **Losing Condition**: If you collect numbers out of order, you lose.

### Implementation Algorithm
1. **Initialization**: A grid-based board is created with a border and random positions for numbered tiles.
2. **Player Movement**: The player can move using `w`, `a`, `s`, and `d` keys. The game checks for valid moves within the board boundaries.
3. **Number Collection**: When the player presses `e`, the number at the current position is collected.
   - If all numbers are collected in ascending order, the player wins.
   - If numbers are collected out of order, the player loses.
4. **Game Display**: The board is displayed after each move, showing the player’s position and the state of the tiles.

### Code Description
The game is implemented in Python using the following main components:
- **`getch` Function**: Handles single-character input for cross-platform compatibility.
- **`Board` Class**: Manages the board state, player position, and game logic.
  - **`_cells` Method**: Initializes the board grid.
  - **`set_values` Method**: Randomly places numbered tiles on the board.
  - **`action` Method**: Processes user input and updates the game state.
  - **`print_board` Method**: Displays the board in a visually intuitive format.
- **`run` Function**: Main game loop that updates the board and processes user input.

### Installation
1. **Requirements**:
   - Python 3.8 or later
   - A terminal or command-line interface

2. **Setup**:
   - Clone or download the script to your local machine.
   - Ensure Python is installed and accessible from the command line.

### Execution
1. Open a terminal or command-line interface.
2. Navigate to the directory containing the script.
3. Run the script using the command:
   ```bash
   python3 grid_base.py
   ```
4. Follow the on-screen instructions to play the game.

### Example Usage
1. Start the game by running the script.
2. The initial board is displayed with numbers and the player position (`🟦`).
3. Use the movement controls (`w`, `a`, `s`, `d`) to navigate the board.
4. Press `e` to collect numbers in the correct order.
5. Continue until you either win or lose.

### Troubleshooting
- **Input Issues**: If the controls do not respond as expected, ensure your terminal supports raw input mode.
- **Compatibility**: For Windows users, the `msvcrt` module is used for input handling. Linux and macOS users rely on `termios` and `tty` modules.

### Notes
- The board size can be adjusted in the `run` function by changing the parameter passed to `Board(size)`. The default size is 10.
- The script is designed for educational purposes and can be extended or modified for additional features.

### Example OutPut:
```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹3 🟪🟪🟪🟦🟪🟪🟪🟪🟪🔹
🔹2 🟪🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟨🟨🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟨🟪🟪🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🟨🟪🔹
🔹🟪🟪1 🟪🟪🟪🟪🟪🟪🟪🔹
🔹🟨🟨🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🟪🟪🟪🟪🟨🟪🟪🟪🟪🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
```
