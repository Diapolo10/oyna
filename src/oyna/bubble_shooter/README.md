# Documentation for Bubble Shooter Game

## Overview of the Game
Bubble Shooter is a dynamic arcade-style game where players aim to shoot colored bubbles into a grid of existing bubbles. The objective is to clear matching groups of bubbles by forming clusters of three or more bubbles of the same color. The game challenges your strategy and reflexes as new bubbles continuously appear, gradually moving closer to the player’s position.

## How to Play
1. **Objective**: Clear as many bubbles as possible by shooting bubbles of the same color into groups.
2. **Controls**:
   - **W**: Shoot the bubble upward.
   - **A**: Move the shooter left.
   - **D**: Move the shooter right.
   - **S**: Change the color of the bubble being shot.
3. **Game Loop**:
   - Aim to shoot bubbles of the same color to form a cluster of three or more.
   - Avoid letting the bubbles reach your position; otherwise, the game ends.
4. **Scoring**: Points are awarded based on the number of bubbles cleared. The score is displayed at the bottom of the screen.

## Code Implementation
The code is structured into several classes and functions for modularity and ease of understanding.

### Key Components
1. **`State` Enum**:
   - Defines various states of the game, such as different bubble colors, walls, and the end state.
   - Provides a visual representation of each state using emojis.

2. **`Cell` Class**:
   - Represents a single cell in the grid.
   - Tracks the cell’s state (e.g., empty, bubble, or wall) and neighboring cells (up, down, left, right).

3. **`Board` Class**:
   - Manages the game grid and all game logic, including:
     - Initializing the grid with walls and bubbles.
     - Handling player movement and bubble shooting.
     - Detecting and clearing matching bubbles.
     - Spawning new bubbles at regular intervals.
     - Shifting rows downward as the game progresses.
   - Includes helper functions for collision detection, bubble matching, and bubble clearing.

4. **`run` Function**:
   - Starts the game loop.
   - Listens for keyboard inputs using the `pynput` library.
   - Updates the board state and renders the grid in the terminal.

### Game Algorithm
1. **Initialization**:
   - Create a `Board` instance with a predefined size.
   - Populate the top portion of the grid with random bubbles.
   - Place the player at the bottom center with a randomly colored bubble.

2. **Game Loop**:
   - Continuously listen for user input.
   - Update the board state based on the input:
     - Move the shooter left or right.
     - Shoot the bubble upward and check for matches.
     - Change the bubble’s color.
   - Periodically add new rows of bubbles at the top.
   - Clear any "zombie" (unreachable) bubbles.

3. **Match Detection**:
   - When a bubble lands, check if it forms a cluster of three or more bubbles of the same color in any direction (horizontal, vertical, or diagonal).
   - If a match is found, remove those bubbles from the grid.

4. **End Condition**:
   - The game ends when bubbles reach the player’s position.

### Example Gameplay
When you run the script:
- The terminal will display the grid with bubbles and the shooter.
- Use the controls to position and shoot bubbles to clear the grid.
- The game continues until bubbles reach the shooter’s position.


## Dependencies
- **Python 3.10+**
- **`pynput` Library**: Used to capture keyboard inputs.

## Running the Game
1. Install the required dependencies:
   ```bash
   pip install pynput
   ```
2. Run the script:
   ```bash
   python bubble_shooter.py
   ```
3. Enjoy the game!

## Game Example:
```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹🔵🟡🟣🔴🔴🟡🟣🟣🔵🔴🔵🟣🔴🟣🔵🔹
🔹⚪️⚪️🟡🟡🟣🔴🟣🟡🟣🔵🔴🟡⚪️🔴🔵🔹
🔹⚪️🟡🔴🟡🟣🔵⚪️⚪️⚪️🟡🔴🔵🟣🔴⚪️🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹                               🔹
🔹               🟡              🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
Scores: 5
```
Feel free to share feedback or contribute to improving the game!
