### Game Documentation: Tic-Tac-Toe with AI

#### Game Overview:
This is a console-based Tic-Tac-Toe game, where you play against an AI opponent. The game is played on a nxn( default 3x3) grid, where each player (you and the computer) takes turns to mark a cell with an "X" or "O". The objective is to get three of your marks in a row, either horizontally, vertically, or diagonally. The game will continue until there is a winner, a draw, or the game is exited.

#### How to Play:
- You control the "X" (❌) and the computer controls the "O" (⭕️).
- You can move using the following keys:
  - **w**: Move up
  - **a**: Move left
  - **s**: Move down
  - **d**: Move right
  - **e**: Place your mark at the current position
  - **Space**: Exit the game
- The game ends when either you or the computer win (3 marks in a row), the board is full (a draw), or you choose to exit.

#### Installation and Execution:
To run the game on your system:

1. **Install Python**:
   Ensure that you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Run the Game**:
   - Open a terminal (or Command Prompt on Windows) and navigate to the related folder.
   - Run the game by typing the following command:
     ```bash
     python grid_base.py
     ```
   - The game will start and will ask you for input based on the commands mentioned earlier.

#### Algorithm Description:
The game follows a simple structure with the following core elements:

1. **Board Representation**:
   - The game board is represented as a 2D grid, with the edges marked as walls (`🔹`), and the inside cells initially empty (`  `).
   - The player starts at the center of the grid, and the AI moves afterward.

2. **Player Input**:
   - You can control the movement of your piece and place it on the board using the 'w', 'a', 's', 'd', and 'e' keys.
   - The game accepts your action, checks for a win condition, and if it's not the player's turn to place a mark, it allows the computer to take its turn.

3. **AI Logic (Minimax Algorithm)**:
   - The AI uses the **Minimax Algorithm** to decide its move. This algorithm explores all possible moves, simulates both player and computer moves, and chooses the best move based on the highest possible score.
   - It also uses **Alpha-Beta Pruning** to reduce the number of unnecessary moves it checks, making the game run faster.

4. **Game States**:
   - The game ends in three possible states: **Win**, **Loss**, or **Draw**.
   - After each move, the game checks if any player has won (3 marks in a row) or if the board is full, resulting in a draw.

5. **Game Display**:
   - The board is displayed in the terminal with colored symbols for clarity. The player's position is highlighted in a distinct color.

6. **Exit Option**:
   - Press the **Space** key to exit the game anytime during gameplay.

#### Code Breakdown:
1. **Imports**:
   - `enum`: Used for defining constant values for the game (e.g., Emoji for marks like `❌`, `⭕️`).
   - `math`, `random`, `platform`, `sys`: These libraries help with the AI logic, random moves, and platform-specific functionalities.
   - `termios`, `tty`: Handle the input for characters without pressing Enter (works on Unix-like systems).

2. **Classes and Methods**:
   - **Emoji**: Defines symbols for the player, computer, walls, and results (win/loss/draw).
   - **Board**: Contains all the logic for the game board, including cell management, checking for winners, and AI moves.
     - `action()`: Handles player movement and input.
     - `play_game()`: Updates the game after each move.
     - `minimax()`: Implements the Minimax Algorithm for the AI to calculate the best move.
     - `computer_move()`: Determines and executes the computer’s move using Minimax.

3. **Main Function** (`run()`):
   - The game loop that runs until the game ends or is exited. It continuously updates the board and accepts player input.

#### Example of How to Play:
1. The game starts with the board looking like this (with walls and empty cells):
   ```
   🔹🔹🔹🔹🔹
   🔹      🔹
   🔹      🔹
   🔹      🔹
   🔹🔹🔹🔹🔹
   ```

2. The player moves their piece (❌) using the keys **W**, **A**, **S**, and **D** to navigate, and **E** to place the mark.

3. After the player makes a move, the computer (⭕️) will automatically make its move.

4. If you get three marks in a row, either horizontally, vertically, or diagonally, you win! If the board fills up without a winner, it's a draw.

5. You can exit anytime by pressing the **Space** bar.

#### Example Output:
```
🔹🔹🔹🔹🔹
🔹      🔹
🔹 ❌   🔹
🔹    ⭕️🔹
🔹🔹🔹🔹🔹

Your Move (WASD to move, E to place, Space to exit):
```

#### Conclusion:
This Tic-Tac-Toe game offers a fun challenge with an AI opponent that uses a sophisticated algorithm to compete. Whether you're a beginner or an advanced user, the game can be enjoyed by anyone who likes strategic games.
