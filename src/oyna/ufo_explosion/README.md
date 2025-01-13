# UFO Explosion

## Game Overview:
The **UFO Explosion** is a simple text-based game where the player controls a UFO (🛸) moving across a grid to avoid obstacles and reach a destination. The goal is to navigate through the grid, moving the UFO using keyboard input, and destroyed a castle (🏠).


## [grid base](./grid_base.py)
### How to Play:
- You control the UFO (🛸) by moving it across the board.
- The board consists of a grid where you can move the UFO right.
- The game randomly places a castle (🏠) on the board. Your goal is to destroyed it.
- You control the UFO’s movement by entering a number (which indicates how many steps to move the UFO).
- If you crash into the walls or castle, your UFO will explode (💥), and the game will reset.

### Controls:
- **Enter a number:** The number you enter will move the UFO that many steps across the grid. For example, if you type `3`, the UFO will move 3 * `game size // 2` steps forward for default 3 * 7 characters.
- **Exit the game:** If you enter any character other than a number, the game will exit.

### Game Algorithm:
1. **Board Setup:**
   - The game board consists of a grid where the UFO starts at a specific position.
   - The outer boundary of the grid is made of walls (🔹).
   - The player moves the UFO across the grid, and the game randomly generates a castle (🏠) at different locations.

2. **UFO Movement:**
   - The UFO can move in the right direction depending on the number you input.
3. **Explosion (Boom):**
   - If the UFO hits a wall or a castle, it explodes (💥).
   - After the explosion, the UFO resets to its starting position, and the board is updated.

4. **Castle Creation:**
   - The game randomly places a castle (🏠) on the board at a different location each time the UFO resets.

5. **Game Reset:**
   - After the UFO explodes, it resets, and the game continues until the player exits.

### How to Install and Run:
#### Requirements:
- Python 3.x

#### Installation:
1. **Install Python**: Ensure that you have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/.

#### Running the Game:
1. **Download or Copy the Code**: Copy the provided Python code into a file, for example, `grid_base.py`.

2. **Run the Game**: Open your terminal or command prompt, navigate to the folder where the file is saved, and run the game with the following command:
   ```bash
   python grid_base.py
   ```

3. **Play the Game**: Once the game starts, input a number to move the UFO. If you crash, the game will reset. To exit, enter any non-numeric character.

### Code Explanation:

#### Key Classes and Functions:

1. **getch()**: A function that captures a single key press from the user. It works differently on Windows (`msvcrt` module) and Unix-based systems (`termios` and `tty` modules).

2. **Board Class**:
   - **`__init__()`**: Initializes the game board with walls (🔹), empty spaces, and a UFO (🛸).
   - **`_cells()`**: Creates the grid and sets the walls around the edges.
   - **`action()`**: Handles user input (number for movement or any other input to exit).
   - **`move()`**: Moves the UFO a certain number of steps based on user input.
   - **`_boom()`**: Resets the UFO’s position if it crashes into an obstacle, showing an explosion (💥).
   - **`create_castle()`**: Randomly places a castle (🏠) on the board.
   - **`__str__()`**: Provides a string representation of the game board, updating the display after each move.

3. **run()**: The main function that starts the game. It initializes the board and continuously waits for user input to move the UFO or exit the game.

#### How the Game Works:
- The board is displayed using a grid of cells, where the UFO (🛸) is placed at the starting position.
- The player inputs a number to move the UFO across the grid.
- The UFO moves in a diagonal pattern depending on the input number.
- If the UFO collides with a castle (🏠) or the walls (🔹), an explosion (💥) happens, and the game resets the UFO's position.
- A new castle is generated in a random location after each reset.

### Troubleshooting:
- **If the game doesn’t start**: Ensure that Python is installed correctly and that you are using the correct command to run the script.
- **If the controls don’t work**: Make sure to enter numeric values to move the UFO. Non-numeric characters will exit the game.

---

Enjoy playing **UFO Escape**, and try to navigate the UFO as far as you can without hitting any obstacles!
