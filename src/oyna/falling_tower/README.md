### Falling Tower

---

#### **Introduction**
This is a simple terminal-based falling-block game where the player controls a moving block that must catch falling blocks. The game increases in difficulty as the space between the falling blocks narrows. It provides a fun and quick challenge, combining strategy and timing.

---

### **How to Play**
1. **Objective**:
   - Catch the falling blocks with your moving block. The game ends if you fail to align your block with the falling blocks or if the space between the blocks is completely closed.

2. **Controls**:
   - Use **any key** on the keyboard to make the falling blocks descend one step.

3. **Gameplay Flow**:
   - Your block automatically moves left and right along the screen.
   - Press a key to make the falling blocks descend.
   - Align your moving block with the falling blocks to survive.

4. **Winning**:
   - The game continues indefinitely, and your goal is to survive as long as possible.

---

### **Code Algorithm**
1. **Game Board Initialization**:
   - The board is represented as a 2D grid with walls (`🔹`), empty spaces (`  `), and blocks (`🟪`).

2. **Player Movement**:
   - The player’s block automatically moves left and right on the screen.
   - When reaching the edges of the grid, the block reverses direction.

3. **Falling Blocks**:
   - Blocks fall one row at a time when the user presses a key.
   - The space between the falling blocks narrows over time, making the game more challenging.

4. **Collision Detection**:
   - If the falling blocks reach the player’s row and are not aligned with the player’s block, the game ends.

5. **Game Update**:
   - The board is redrawn at each step to reflect updated positions of the blocks and player.

---

### **Installation and Setup**
1. **Prerequisites**:
   - Python 3.10 or higher must be installed.
   - Install the required library `pynput` using the command:
     ```bash
     pip install pynput
     ```

2. **Clone or Download the Code**:
   - Save the script as a `.py` file, for example, `grid_base.py`.

3. **Run the Game**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the game script is saved.
   - Run the game using:
     ```bash
     python grid_base.py
     ```

---

### **How the Code Works**
1. **Game Objects**:
   - `State`: Enum defining various states of the board (walls, empty cells, blocks).
   - `Board`: Handles the creation of the game grid, block positioning, player movement, and game updates.

2. **Game Logic**:
   - The player’s block moves automatically, controlled by `move_to_left` and `move_to_right` methods.
   - The `fall` method updates the position of the falling blocks and adjusts the alignment with the player’s block.
   - The `update` method manages the game loop by redrawing the grid, checking for input, and handling collisions.

3. **Keyboard Listener**:
   - Uses `pynput` to detect any key press, triggering the falling block's descent.

4. **Main Loop**:
   - Continuously updates the board and redraws it until the game ends.

---

## Example OutPut:
```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹                                       🔹
🔹                  🟪                   🔹
🔹                                       🔹
🔹                                       🔹
🔹                                       🔹
🔹                                       🔹
🔹                                       🔹
🔹                                       🔹
🔹                                       🔹
🔹                                       🔹
🔹                                       🔹
🔹                    🟪                 🔹
🔹                    🟪🟪               🔹
🔹                  🟪🟪🟪               🔹
🔹                  🟪🟪🟪🟪             🔹
🔹              🟪🟪🟪🟪🟪🟪             🔹
🔹              🟪🟪🟪🟪🟪🟪🟪           🔹
🔹              🟪🟪🟪🟪🟪🟪🟪           🔹
🔹              🟪🟪🟪🟪🟪🟪🟪🟪         🔹
🔹            🟪🟪🟪🟪🟪🟪🟪🟪🟪         🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
```

Enjoy the game! 🎮
