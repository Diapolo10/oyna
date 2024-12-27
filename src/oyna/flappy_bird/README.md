# [Flappy Bird](https://en.wikipedia.org/wiki/Flappy_Bird)

**About the Game**

From Wikipedia, the free encyclopedia


Flappy Bird is a 2013 casual mobile game developed by Vietnamese video game artist and programmer Dong Nguyen (Vietnamese: Nguyễn Hà Đông), under his game development company .Gears. The game is a side-scroller where the player controls a bird attempting to fly between columns of green pipes without hitting them. The player's score is determined by the number of pipes they pass. Nguyen created the game over a period of several days, using the bird from a cancelled game made in 2012.

The game was released in May 2013 but received a sudden spike in popularity in early 2014, becoming a sleeper hit. Flappy Bird received poor reviews from some critics, who criticized its high level of difficulty and alleged plagiarism in graphics and game mechanics, while other reviewers found it addictive. At the end of January 2014, it was the most downloaded free game in the App Store for iOS. During this period, its developer said that Flappy Bird was earning $50,000 a day from in-app advertisements as well as sales.

Flappy Bird was removed from both the App Store and Google Play on February 10, 2014, with Nguyen claiming that he felt guilty over what he considered to be the game's addictive nature and overusage. Its popularity and sudden removal caused phones with the game installed before its removal to be put up for sale for high prices over the Internet. Clones of Flappy Bird became popular on the App Store after the original app's removal, and both Apple and Google have removed games from their app stores for being too identical.

In August 2014, a revised version of Flappy Bird, called Flappy Birds Family, was released exclusively for the Amazon Fire TV. Bay Tek Games also released a licensed coin-operated Flappy Bird arcade game.


"Flappy Bird" is a text-based survival game where the player (represented by a 🐣 symbol) must avoid falling blocks (🟪) by moving up or down within a confined space. The game ends if the player collides with a block, represented by a 💥 symbol.

---

## **How to Play**

1. **Goal**: Stay alive as long as possible by avoiding the falling blocks.
2. **Controls**:
   - Press any key to move the player upward.
   - If no key is pressed, the player will automatically move downward.
3. **Scoring**: Your score increases the longer you survive.
4. **Game Over**: The game ends if the player collides with a block.

---


## **Algorithm Overview**
1. **Game Board**:
   - The board is a grid of cells.
   - Each cell can hold an empty space (  ), wall (🔹), player (🐣), block (🟪), or end state (💥).
   - The walls keep the player confined, while the blocks fall from the right edge of the grid to the left.

2. **Game Logic**:
   - The player moves up or down depending on user input.
   - New blocks are created randomly, with gaps to allow the player to pass through.
   - Blocks move leftward, and if a block reaches the player, the game ends.

3. **Gameplay Loop**:
   - The game updates every 0.2 seconds.
   - The player's position, blocks, and score are updated in each step.

---

## **Installation and Setup**

### **Requirements**
- Python 3.10 or higher.
- `pynput` library for handling keyboard inputs.

### **Installing Dependencies**
Run the following command to install the `pynput` library:

```bash
pip install pynput
```

---

## **How to Run the Game**

1. Save the code into a file named `grid_base.py`.
2. Open a terminal in the same directory as the file.
3. Run the game using the command:

```bash
python grid_base.py
```

4. Enjoy the game! Your score will be displayed at the bottom.

---

## **Game Structure**

### **Main Classes and Functions**
- **`State`**: Defines the possible states of a cell (e.g., EMPTY, BLOCK, WALL, PLAYER, END).
- **`Cell`**: Represents a single cell on the board.
- **`Board`**:
  - Initializes the game grid and places the player and walls.
  - Handles player movement, block creation, and block movement.
- **`run()`**: The main function that starts and runs the game loop.

### **Key Features**
- **Keyboard Input**: The game listens for keypresses to control the player's movement.
- **Dynamic Blocks**: Blocks appear at random intervals, adding a challenge to the game.
- **Game Over Condition**: If the player collides with a block, the game ends.

---

## **Example Gameplay**

When the game starts, you'll see something like this:

```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹  🐣            🟪           🔹
🔹                🟪           🔹
🔹                🟪           🔹
🔹                🟪           🔹
🔹                             🔹
🔹                             🔹
🔹                             🔹
🔹                🟪           🔹
🔹                🟪           🔹
🔹                🟪           🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹

        Your(🐣) Scores: 0
```

Press keys to move 🐣 upward. Survive as long as possible to achieve a high score!

---

Feel free to expand this game or customize it as you like!
