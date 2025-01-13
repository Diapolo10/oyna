# Memory Matching

## Introduction
Memory Maze is a puzzle game that combines spatial navigation with memory-based challenges. The player must navigate a grid to uncover and match hidden emoji tiles. The goal is to match all pairs of emojis while avoiding obstacles and walls.

## [grid base](./grid_base.py)


### **How to Play**
1. **Controls:**
   - **`w`**: Move up.
   - **`a`**: Move left.
   - **`s`**: Move down.
   - **`d`**: Move right.
   - **`e`**: Interact with the current tile (select or match).
   - **Spacebar**: Quit the game.

2. **Gameplay:**
   - Navigate the grid using the controls.
   - Reveal a tile by pressing `e`. If you select two matching tiles, they are marked as solved.
   - If the tiles do not match, you can retry until all pairs are solved.
   - The game is won when all tiles are matched.

3. **Winning Condition:**
   - Match all the emoji tiles successfully. Upon completion, the player wins, and the maze celebrates with a trophy emoji!



### **Code Overview**
The game uses Python and employs classes and enums to represent the game components. Below is a high-level explanation:

1. **Key Components:**
   - **`State` Enum**: Represents different cell states (e.g., wall, block, player, solved, win).
   - **`Cell` Class**: Represents each cell in the grid with properties like state, neighbors, and emoji value.
   - **`Board` Class**: Handles grid creation, player movement, tile matching, and game logic.

2. **Algorithms:**
   - The grid is created with walls surrounding the playable area.
   - Emoji pairs are randomized and placed within the grid.
   - Player actions (move, select, match) update the board dynamically.
   - The game checks for winning conditions after every move.



### **Installation**
1. **Prerequisites:**
   - Python 3.10 or higher must be installed on your system.


2. **Dependencies:**
   - The game uses standard Python libraries, so no external packages are required.



### **Running the Game**
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `grid_base.py` file.
3. Run the command:
   ```bash
   python grid_base.py
   ```
4. Enjoy playing Memory Maze!



### **Tips for Success**
- Memorize the positions of the emojis as you reveal tiles.
- Plan your moves to minimize backtracking.
- Avoid mismatching tiles repeatedly to save time.



### Example Output:
```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🔸🟪🟪🔸🟪🟪🟪🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟦🟪🔹
🔹🟪🔸🟪🔸🟪🔸🟪🟪🔹
🔹🟪🟪🟪🔸🟪🟪🦄🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
```

Feel free to share feedback or customize the game by modifying the code!
