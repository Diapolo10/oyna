
# Snakes and Ladders Game

This is a console-based game where two players—represented by a cat (😸) and a dog (🐶)—race to reach the destination marked by a candy (🍭) while navigating obstacles and using ladders. Let’s dive into how to play and set up the game.



## 🎮 About the Game

This is a two-player board game where the goal is to navigate from the start to the destination using dice rolls. Along the way, players may encounter ladders that can either help or hinder their progress. The game board is dynamic and includes obstacles, directions, and ladders, ensuring each game is a unique experience!

## [grid base](./grid_base.py)


### 🚀 How to Play

1. **Game Start**: The game begins with both players at the bottom-left corner of the board.
2. **Player Moves**:
   - Press any key to roll the dice.
   - The number rolled determines how many steps you move in the direction shown on the board.
   - If you land on a ladder, it will automatically move you up, down, left, or right.
3. **Winning the Game**: The first player to reach the candy (🍭) wins the game!
4. **Enemy Moves**: The enemy (🐶) moves automatically after the player’s turn.

**Note**: You can press the space bar (` `) to end your turn without moving.



### 💻 Algorithm Overview

The game logic follows these steps:
1. **Initialization**:
   - The board is generated as a grid of cells.
   - Walls, ladders, and the destination are placed randomly.
2. **Player and Enemy Movement**:
   - Dice rolls determine the number of steps to move.
   - Players follow directional cues (up, down, left, right).
   - Ladders automatically transport players if landed upon.
3. **Win Condition**:
   - The game checks after every turn if a player has reached the destination.



### 🛠️ Installation and Setup

1. **Requirements**:
   - Python 3.9 or higher.

2. **Run the Game**:
   ```bash
   python grid_base.py
   ```



## #📝 Controls and Tips

- **Roll the Dice**: Press any key to roll the dice and move.
- **View Progress**: The board updates in real-time to show the players’ positions.
- **Winning Tip**: Pay attention to the ladders—they can speed up your progress or slow you down!



### 📊 Board Elements

| Symbol  | Meaning                                   |
| ------- | ------------------------------------------ |
| 🟪       | Regular block                             |
| 🍭       | Destination (goal)                        |
| 🔹       | Wall (impassable)                         |
| ⏫ ⏬ ⏪ ⏩ | Ladders (move in the indicated direction) |
| 😸       | Player (You)                              |
| 🐶       | Enemy (Opponent)                          |
| (empty) | End of game                               |



### 🔍 Example Gameplay

- Start the game.
- The player (😸) rolls a dice and moves 3 steps in the indicated direction.
- The enemy (🐶) rolls their dice and moves automatically.
- If either lands on a ladder (⏫, ⏬, ⏪, ⏩), they are moved to the corresponding cell.
- The game continues until one player reaches the candy (🍭).

```
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
🔹🍭🟪🟪⏬🟪🟪🟪⏪🟪🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪⏬⏪🟪🔹
🔹🟪⏬🟪⏬⏬🟪🟪🟪🟪🟪🔹
🔹🟪⏩🟪🟪⏪⏫⏩🟪🟪🟪🔹
🔹🟪🟪⏪🟪🟪⏩🟪🟪⏩🟪🔹
🔹🟪🟪⏩🟪⏩🟪🟪⏫⏩⏬🔹
🔹🟪⏬🟪🟪🟪⏬🟪⏬🟪⏪🔹
🔹🟪🟪🟪🟪⏬⏬⏬🟪🟪🟪🔹
🔹🟪🟪🟪⏫🟪⏬😸🟪🐶🟪🔹
🔹🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🔹
🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹
 You 😸: 2 Enemy  🐶: 1
 ```



Enjoy the game! If you encounter any issues or have suggestions, feel free to reach out.
