### Documentation for the Game Code

---

#### **Game Description**
This is a simple text-based grid game where the player navigates a board using keyboard input. The goal is to reach the target emoji (which is different from other emojis
).
---

#### **How to Play**
1. **Start the Game:**
   - Run the script to initialize the game board.
   - The player (`🟦`) starts in the middle of the grid.
2. **Controls:**
   - Use the following keys to move the player:
     - `w`: Move up
     - `a`: Move left
     - `s`: Move down
     - `d`: Move right
   - Press `e` to interact with the current tile:
     - If the player is on the `ANSWER` tile, they win (`🏆`).
     - Otherwise, it shows an incorrect answer (`🟥`).
   - Press the space bar (` `) to exit the game.
3. **Objective:**
   - Navigate to the emoji which is different from other emojis
 tile.
1. **Game Ends:**
   - You win if you reach the `ANSWER` tile.
   - You can also exit manually by pressing the space bar.

---

#### **Code Algorithm**
1. **Game Initialization:**
   - The `Board` class creates a grid of cells (`size x size`) with walls around the edges.
   - One cell is randomly designated as the `ANSWER` tile.
   - The player starts at the center of the grid.
2. **Player Movement:**
   - The `action` method handles the player's moves based on keyboard input.
   - It checks the next cell for walls and prevents the player from moving into them.
3. **Win or Exit:**
   - If the player interacts (`e`) with the `ANSWER` tile, they win.
   - If the player presses the space bar, the game ends without a win.
4. **Randomized Features:**
   - The `ANSWER` tile is placed at a random position on the board at the start.
   - Emojis for the `ANSWER` and `BLOCK` tiles are randomized.

---

#### **Installation and Setup**
1. **Prerequisites:**
   - Python 3.10 or higher.
   - Required only Python standard libraries .
2. **Installation:**
   - Ensure Python is installed and added to your system's PATH.
3. **Running the Game:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script with the command:
     ```bash
     python grid_base.py
     ```

---

#### **Customizations**
- **Grid Size:**
  - Modify the `size` parameter in `Board` initialization to change the game board's dimensions.
- **Emojis:**
  - Add or replace emojis in the `selected_emoji` list to change the appearance of the game.
- **Player Start Position:**
  - Adjust the `player` attribute in the `Board` class to change the initial location.

---

#### **Known Issues**
- The game currently uses blocking input methods, which may not work well in some IDEs. Running the game in a terminal is recommended.
- For non-Windows systems, `getch` uses a custom implementation that may behave differently on some Linux distributions.

---

Enjoy the game and happy navigating! 🎮
