# Game Documentation: Dino Game

## Game Overview:
The **Dino Game** is a simple text-based game where the player controls a character (represented by a chick, 🐥) who must avoid cactus obstacles (🌵) on a moving board. The player can move the chick up or down to avoid collisions. If the chick hits a cactus, the game ends. The objective is to survive as long as possible and score points by dodging the cacti.

## How to Play:
- The player controls a chick (🐥) on a grid.
- The chick moves up or down based on user input (from the keyboard).
- Cacti (🌵) randomly appear on the board and move from right to left.
- The player must avoid the cacti; if they collide with one, the game ends.
- The goal is to survive as long as possible and score points based on how many steps the chick survives.

### Controls:
- **Any Key (↑):** Move the chick up.

## Game Algorithm:
1. **Board Setup:**
   - The game board is a grid where walls (🔹) form the edges.
   - The board consists of cells, and each cell can have one of several states: **BLOCK**, **CACTUS**, **WALL**, **PLAYER**, or **END**.
   - The player's character (🐥) starts near the bottom of the board.

2. **Player Movement:**
   - The player can move up or down by pressing the any keys. The chick's position is updated based on user input.

3. **Cactus Movement:**
   - Cacti (🌵) appear at random intervals and move from right to left across the screen.
   - If a cactus reaches the player, the game ends.

4. **Game Over:**
   - The game ends if the player collides with a cactus (🌵).

5. **Game Continuation:**
   - The game continues to run, and the player's score increases the longer they avoid cacti.

## How to Install and Run:
### Requirements:
- Python 3.x
- `pynput` library (for capturing keyboard input)

### Installation:
1. **Install Python**: Ensure you have Python 3.x installed on your machine. You can download it from the official Python website: https://www.python.org/downloads/

2. **Install pynput**: The game uses the `pynput` library to capture keyboard input. Install it using the following command:
   ```bash
   pip install pynput
   ```

### Running the Game:
1. **Run the Game**: In your terminal, navigate to the folder where the file is located and run the game using:
   ```bash
   python grid_base.py
   ```

2. **Play the Game**: Once the game starts, use the **up** and **down** arrow keys to move the chick and avoid the cacti.

## Code Explanation:

### Key Classes and Functions:

1. **State (Enum)**: Defines various states for the cells in the game (BLOCK, CACTUS, WALL, PLAYER, END).

2. **UserInput (Dataclass)**: Stores the current value of the player's input (whether to move up or down).

3. **Cell (Class)**: Represents a single cell on the game board. Each cell can contain different states, like WALL, CACTUS, or PLAYER.

4. **Board (Class)**: Represents the game board. It manages the grid, the player's position, and the cactus movement. The board is initialized with walls and player cells.

5. **Game (Class)**: The main game class that handles the game loop. It listens for keyboard input, updates the board, moves the player and the cacti, and checks for collisions.

6. **set_user_input (Function)**: Updates the player's input when a key is pressed. If a valid key is pressed, it modifies the player's movement state.

7. **Listener**: Listens for keyboard input to control the player's movement up and down during the game.

### Important Functions:
- **move()**: Moves the player and the cacti on the board each step.
- **_move_player()**: Moves the player up or down based on user input.
- **_create_new_cactus()**: Adds new cacti to the board at random intervals.
- **_move_cactus()**: Moves the cacti from right to left. If a cactus reaches the player's position, the game ends.

## Example OutPut:
```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹                                                                             🔹
🔹                                                                             🔹
🔹                                                                             🔹
🔹                                                                             🔹
🔹                                                                             🔹
🔹                                                                             🔹
🔹                                                                             🔹
🔹    🐥              🌵          🌵                      🌵          🌵       🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹

    Your(🐥) Scores: 56
```
## Troubleshooting:
- **If the game doesn't start:** Ensure Python and `pynput` are correctly installed.
- **If the controls don't work:** Make sure you are pressing the correct keys (up or down arrows) to move the chick.

---

Enjoy the game, and try to get the highest score by dodging as many cacti as you can!
