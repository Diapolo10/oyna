# Sudoku


## Game Overview

This is a **text-based Sudoku game** where the player interacts with the board to fill in numbers while adhering to the classic Sudoku rules. The game is implemented in Python, and the board layout is dynamically generated. The objective is to move around a grid, inserting numbers (1-9) into empty cells, avoiding conflicts, and solving the puzzle.

## [grid base](./grid_base.py)
### How to Play

1. **Movement**: The player moves around the grid using the following keys:
    - **`w`**: Move up
    - **`a`**: Move left
    - **`s`**: Move down
    - **`d`**: Move right

2. **Inserting Numbers**: While navigating the grid, the player can insert numbers by pressing:
    - **`1`**: Insert number 1
    - **`2`**: Insert number 2
    - **`3`**: Insert number 3
    - **`4`**: Insert number 4
    - **`5`**: Insert number 5
    - **`6`**: Insert number 6
    - **`7`**: Insert number 7
    - **`8`**: Insert number 8
    - **`9`**: Insert number 9

3. **Exit**: Press the **`Space`** key to end the game.

### Algorithm Implementation

1. **Board Setup**:
    - The game creates a **3x3 Sudoku grid** using cells that may contain numbers (1-9), walls, or be empty.
    - The grid is filled with numbers, and some of them are marked as **fixed** (not editable by the player).

2. **Cells**:
    - Each cell in the board can have different states such as `EMPTY`, `PLAYER`, `INTERNAL_WALL`, `EXTERNAL_WALL`, `FIXED_NUMBER`, and `END`.
    - The player is represented by a special marker ("🟦") that moves around the grid.

3. **Movement**:
    - The player can move up, down, left, or right unless blocked by a wall. The player’s position is updated as they move through the grid.

4. **Input Handling**:
    - The game reads input from the player (e.g., key presses for movement and number insertion) and updates the state of the game accordingly.
    - The game keeps track of the player's actions, validating their moves and numbers.

5. **End Condition**:
    - The game ends when the player solved the puzzle.

### How to Install and Run the Code

To run this game, you'll need to have Python installed on your machine. Follow the steps below to get started:

1. **Install Python**:
    - Ensure that you have **Python 3.10 or higher** installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Run the Game**:
    - Open a terminal or command prompt in the directory where your `grid_base.py` file is saved.
    - Run the game by executing:
      ```bash
      python grid_base.py
      ```

3. **Playing the Game**:
    - Once the game is running, use the keyboard to navigate the grid and fill in numbers.
    - Follow the instructions on the screen to play and solve the puzzle.

### Code Structure and Explanation

1. **Imports**:
    - `enum`: Used for defining states and actions.
    - `random`: Used for randomizing the board setup.
    - `typing.Optional`: Used for type hinting optional values for cells.

2. **Classes**:
    - `State`: An enumeration of different cell states (empty, player, wall, fixed number, etc.).
    - `Action`: An enumeration of different actions a player can take (move, insert numbers, exit).
    - `Cell`: Represents a single cell in the Sudoku grid, handling its state, value, and neighboring cells.
    - `Board`: The main class for setting up and managing the Sudoku board. It includes logic for placing walls, setting numbers, and handling player input.

3. **Game Loop**:
    - The game runs in a loop, where it continuously checks for player input, updates the board, and prints the updated state to the screen.


### Example Output:
```
🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸
🔸      🔹 8 5 4🔹 2 3   🔸
🔸   3  🔹      🔹      4🔸
🔸 5 8 4🔹      🔹       🔸
🔸🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔸
🔸 3    🔹   9  🔹      5🔸
🔸 8   5🔹 6    🔹 9    1🔸
🔸      🔹   8  🔹    6 2🔸
🔸🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔸
🔸   5 9🔹      🔹       🔸
🔸   2 8🔹 1   3🔹 4    9🔸
🔸   1  🔹 5   9🔹 7     🔸
🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸
```
