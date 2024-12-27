# Snake Game Documentation

## Overview
This is a simple implementation of the classic Snake game using Python. The game runs in the console, where you control a snake that moves around the board, eats apples to grow, and avoids hitting walls or its own body. The game continues until the snake hits a wall or its own body.

### How to Play
- You control the snake using the `w`, `a`, `s`, and `d` keys:
  - `w` moves the snake up.
  - `a` moves the snake left.
  - `s` moves the snake down.
  - `d` moves the snake right.
- The goal is to eat the apples (🍎) that appear on the board. Each apple you eat makes the snake grow longer.
- The game ends when the snake hits a wall (🔹) or its own body (🟪).

## Game Implementation

### 1. **Game Elements (Classes)**

- **State Enum**: Defines the possible states of each cell on the board:
  - `BLOCK`: An empty block where the snake can move.
  - `APPLE`: A cell that contains an apple (🍎).
  - `WALL`: The border of the game area (🔹).
  - `PLAYER`: Part of the snake's body (🟪).
  - `HEAD`: The snake's head (🟨).
  - `END`: Indicates the end of the game when the snake hits something fatal.

- **Direction Enum**: Defines the directions the snake can move:
  - `LEFT`
  - `RIGHT`
  - `DOWN`
  - `UP`

- **Cell Class**: Represents each cell in the game board. Each cell has a state and can have neighboring cells (up, down, left, right) for movement.

- **Board Class**: Manages the game board. It creates the board, places walls, the snake, and apples, and handles movement. The board is a 2D grid of cells, and it has methods to:
  - Set walls around the edges.
  - Set apple positions.
  - Handle the snake's movement.
  - Check for collisions.
  - Update the game state.

- **UserInput Class**: Keeps track of the player's input (direction of movement).

### 2. **Game Algorithm**

- **Board Setup**: The board is created with a specified size. It automatically places walls around the edges and places the snake’s initial position in the center. An apple is placed randomly on the board.

- **Movement**: The snake's head moves in the direction specified by the player. If the snake eats an apple, it grows, and a new apple is placed randomly. If the snake hits a wall or its own body, the game ends.

- **Collision Handling**: When the snake's head moves to a new cell:
  - If the cell contains an apple, the snake eats it and grows.
  - If the cell is a wall or the snake’s own body, the game ends.
  - If the cell is an empty block, the snake simply moves to that cell, and the previous cell becomes empty.

- **Game Loop**: The game runs in a loop where it constantly updates the snake's position, checks for collisions, and redraws the board.

### 3. **Installation and Running the Game**

To run the game, follow these steps:

#### Step 1: Install Python
Ensure that you have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

#### Step 2: Install Dependencies
You will need the `pynput` library for handling keyboard inputs. Install it via pip:
```bash
pip install pynput
```

#### Step 3: Run the Game
1. Save the code into a file, for example, `grid_base.py`.
2. Open a terminal or command prompt in the folder where the file is saved.
3. Run the game by executing:
   ```bash
   python grid_base.py
   ```
4. The game will start in your terminal. Use the `w`, `a`, `s`, `d` keys to control the snake.

### 4. **How to Play**
- Use the arrow keys or `w`, `a`, `s`, `d` to move the snake around the board.
- Try to eat as many apples as possible without hitting the walls or your own body.
- The game will end when the snake crashes into a wall or itself.

### 5. **Game Over**
- When the game ends, the snake will stop moving, and the program will exit. The final state of the board will show the snake’s last position.

### Example Output
```
🔹🔹🔹🔹🔹🔹🔹
🔹🟪🟨    🍎🔹
🔹🟪🟪🟪🟪🟪🔹
🔹🔹🔹🔹🔹🔹🔹
```

In this example:
- The snake is represented by `🟪` and its head is `🟨`.
- The apple is represented by `🍎`.
- The walls are represented by `🔹`.

### Conclusion
This game provides a fun way to practice basic Python programming concepts, including classes, enums, and handling user input. Enjoy playing the Snake game in your console and try to beat your own high score!
