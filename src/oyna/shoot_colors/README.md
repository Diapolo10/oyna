# Shoot Color

## Overview

Shoot Color is a simple game in which the player controls a character that moves across a grid and shoots bubbles of different colors. The goal is to match three or more bubbles of the same color in a row, either horizontally or vertically. If the player successfully makes a match, the bubbles disappear and new bubbles appear, adding an extra layer of challenge. The game continues until the player chooses to exit.

## [grid base](./grid_base.py)

### How to Play

1. **Control the Player:**
   - Use the **`w`**, **`a`**, **`s`**, and **`d`** keys to move the player and shoot bubbles:
     - **`w`**: Shoot the bubble upwards.
     - **`a`**: Move the player to the left.
     - **`s`**: Change the color of the player's bubble.
     - **`d`**: Move the player to the right.

2. **Shoot Bubbles:**
   - The player can shoot bubbles in the direction they are facing.
   - When a bubble is shot, it moves upwards until it hits either a wall or another bubble.
   - If the bubble matches other bubbles of the same color, those bubbles are removed from the grid.

3. **Goal:**
   - The goal is to clear as many bubbles as possible by matching colors and creating combinations.

### Algorithm

- **Game Setup:**
  - The game is played on a grid with walls surrounding the edges. The player starts at the center of the grid and is assigned a random bubble color.
  - The game generates a new bubble at a random location and adds it to the grid.

- **Player Movement:**
  - The player moves left or right by pressing the **`a`** or **`d`** keys.
  - The player can shoot bubbles upwards by pressing the **`w`** key.

- **Bubble Matching:**
  - When a bubble is shot, it moves upwards. If it matches two or more other bubbles of the same color, those bubbles disappear, and the player's score increases.
  - The game also includes a mechanic to change the player's bubble color when the **s** key is pressed.

- **Game Loop:**
  - The game runs in a loop, continuously updating the board, moving the bubbles, and printing the grid to the console. The game ends when the player exits or chooses to stop.

### How to Install and Run the Game

1. **Prerequisites:**
   - Ensure you have Python installed on your machine. This game uses Python 3.x.
   - Install the **pynput** library, which is used for capturing keyboard inputs.

   To install **pynput**, run the following command in your terminal or command prompt:
   ```
   pip install pynput
   ```

2. **Running the Game:**
   - Open your terminal or command prompt, navigate to the directory where the file is located, and run the following command:
   ```
   python grid_base.py
   ```

   The game will start running in your terminal, and you will be able to play by using the keys mentioned earlier (**w**, **a**, **s**, **d**).

### Features

- **Random Bubble Colors:** Every time the player shoots a bubble, the bubble color is randomly selected.
- **Bubble Matching:** Bubbles will disappear when three or more of the same color are aligned.
- **Player Control:** The player can move left or right and shoot bubbles to clear the grid.
- **Dynamic Game Board:** The board continuously updates, and new bubbles are added at random locations.


### Conclusion

Shoot Color is a fun and simple game where you aim to match colored bubbles by controlling a player on a grid. It offers a mix of action and strategy, as you need to think quickly and plan your moves to create bubble combinations and clear the grid.


### Example Output:
```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹⚪️🔴🟡🔴⚪️🔵🟣🔵🟡🟣⚪️🔴🟣🔵🔴🔴🟣🔹
🔹                                 🟣🔹
🔹🟣🔴⚪️🟣🟣🔵🟡🔵🔴⚪️🟣⚪️🔵🟡🟡🟡🔵🔹
🔹🟣                                 🔹
🔹🔵🟡🔴🔵🔵🟡🔵🔵🟡🔵🔵🟡🔴🔵🟣⚪️🔴🔹
🔹                                 ⚪️🔹
🔹⚪️🔴🔵⚪️🔴🔴🟡🔴🟡🟣🔵🔵🔵⚪️⚪️🟡🔴🔹
🔹⚪️                                 🔹
🔹🟡🟡🔵🔴🔴🔵⚪️🔴🔵🟡⚪️⚪️🟣⚪️⚪️🔵🔴🔹
🔹                                 🟡🔹
🔹🟣⚪️🟣🔴⚪️🟣🟡🔵🟡🟣🟣🔵🟡🟣🔵🟡🟣🔹
🔹🔵                                 🔹
🔹🟡🔴🔴🟣⚪️⚪️🟣🟣🟡🟡🔴🟡⚪️🟣🔴⚪️🔴🔹
🔹                                 🟣🔹
🔹      ⚪️🟣🔵🟣🔵🟡🔴🔵🟡🔴🟡🔵🟡🔴🔹
🔹                                   🔹
🔹          🟣                       🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
```
