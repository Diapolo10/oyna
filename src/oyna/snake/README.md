# [Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre))

From Wikipedia, the free encyclopedia


Snake is a genre of action video games where the player maneuvers the end of a growing line, often themed as a snake.

The player must keep the snake from colliding with both other obstacles and itself, which gets harder as the snake lengthens. It originated in the 1976 two-player arcade video game Blockade from Gremlin Industries where the goal is to survive longer than the other player. The concept evolved into a single-player variant where a snake gets longer with each piece of food eaten—often apples or eggs. The simplicity and low technical requirements of snake games have resulted in hundreds of versions—some of which have the word snake or worm in the title—for many platforms.


## [Grid Base:](./grid_base.py)

<div style="text-align: justify;">


### How to Implement
This game is implemented as a grid table where elements are connected with their neighbors through links. Each element of this table contains a `Cell`, Each `Cell` has different states and directions.

By pointing to the head of the snake, which is kept as `head`, if the user chooses a direction, the head of the snake will go to that direction and will inform the rest of the snake's body to move. When moving the head of the snake, it informs the relevant Cell, if the body of the snake reaches this element, it will direct it in a specific direction.


<img align=right style="width:40%;" src="../../../docs/images/snake.png">


### How to Play:
•  Press `w` to move up

•  Press `s` to move down

•  Press `a` to move left

•  Press `d` to move right

•  Press `ctrl + c` to exit


### Requirements:
`pynput`

### How to Run
Run the command: `python ./grid_base.py`
</div>
