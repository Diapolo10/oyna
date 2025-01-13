# Tetris

## Overview
This document provides a detailed guide for the Tetris game implemented in Python. The game is a simplified version of the classic Tetris game, where players control tetrominoes (geometric shapes made up of four squares) that fall from the top of the game board. The objective is to place the tetrominoes strategically to fill rows, which are then cleared to earn points.

## [grid base](./grid_base.py)

### How to Play the Game

### Controls
- **a**: Move the tetromino left
- **d**: Move the tetromino right
- **w**: Rotate the tetromino
- **s**: Drop the tetromino faster

### Rules
1. The game board is a nxm grid where tetrominoes fall from the top.
2. Players must move and rotate the tetrominoes to fit them into empty spaces on the board.
3. The game ends when a new tetromino cannot be placed at the top of the board.


### Prerequisites
- Python 3.x installed on your machine.
- The `pynput` library installed. Install it via pip if not already installed:
  ```bash
  pip install pynput
  ```

### Steps to Run
1. Open a terminal or command prompt and navigate to the directory containing the file.
2. Run the script with the following command:
   ```bash
   python grid_base.py
   ```
3. The game will start, and you can control the tetrominoes using the keyboard.


### Code Explanation

#### Game Board Initialization
- The game board is represented as a nxm grid of zeros. Each cell is either `0` (empty) or `1` (occupied).
  ```python
  board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
  ```

#### Tetris Shapes
- The shapes are defined as 2D lists of ones and zeros. Each list represents a different tetromino.
  ```python
  SHAPES = [
      [[1, 1, 1, 1]],  # I
      [[1, 1], [1, 1]],  # O
      [[0, 1, 0], [1, 1, 1]],  # T
      [[1, 1, 0], [0, 1, 1]],  # S
      [[0, 1, 1], [1, 1, 0]],  # Z
      [[1, 1, 1], [1, 0, 0]],  # L
      [[1, 1, 1], [0, 0, 1]],  # J
  ]
  ```

#### Movement and Rotation
- Functions like `move_left`, `move_right`, `rotate`, and `drop` manage the position and orientation of the tetromino.
- Collision detection is handled by the `can_place` function, ensuring shapes do not overlap or go out of bounds.

#### Clearing Rows
- The `clear_lines` function removes rows that are completely filled and shifts the rows above downward.
  ```python
  def clear_lines() -> None:
      global board
      board = [row for row in board if any(cell == 0 for cell in row)]
      while len(board) < HEIGHT:
          board.insert(0, [0 for _ in range(WIDTH)])
  ```

#### Keyboard Input
- The `pynput` library captures keyboard inputs to control the tetrominoes.
  ```python
  def on_press(key: keyboard.KeyCode) -> None:
      try:
          if key.char == "a":
              move_left()
          elif key.char == "d":
              move_right()
          elif key.char == "w":
              rotate()
          elif key.char == "s":
              drop()
      except AttributeError:
          pass
  ```



### Output
```
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                  🟪🟪                  🔹
🔹                  🟪🟪                  🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                                        🔹
🔹                  🟪🟪🟪🟪              🔹
🔹          🟪🟪      🟪🟪                🔹
🔹          🟪🟪    🟪🟪                  🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
```

### Additional Notes
- **Game Speed**: The game updates every 0.2 seconds. You can adjust the `time.sleep` value to change the speed.
- **Custom Shapes**: You can add more shapes to the `SHAPES` list to enhance gameplay.
- **Error Handling**: Ensure your terminal supports Unicode characters for proper display of the game board.
