# [2048](https://en.wikipedia.org/wiki/2048_(video_game))

From Wikipedia, the free encyclopedia

2048 is a single-player sliding tile puzzle video game written by Italian web developer [Gabriele Cirulli](https://github.com/gabrielecirulli) and published on GitHub. The objective of the game is to slide numbered tiles on a grid to combine them to create a tile with the number 2048; however, one can continue to play the game after reaching the goal, creating tiles with larger numbers. It was originally written in JavaScript and CSS over a weekend, and released on 9 March 2014 as free and open-source software subject to the MIT License. Versions for iOS and Android followed in May 2014.

2048 was intended to be an improved version of two other games, both of which were clones of the iOS game Threes released a month earlier. Cirulli himself described 2048 as being "conceptually similar" to Threes. The release of 2048 resulted in the rapid appearance of many similar games, akin to the flood of Flappy Bird variations from 2013. The game received generally positive reviews from critics, with it being described as "viral" and "addictive".


## [Grid Base:](./grid_base.py)

<div style="text-align: justify;">


### How to Implement
This game is implemented as a grid table where elements are connected with their neighbors through links. Each element of this table contains a `Cell`, a group of 9 of which displays a number.
If a direction is selected, all the elements will move in the selected direction and if their values are equal, they will be merged together.

<img align=right style="width:40%;" src="../../../docs/images/2048.png">


### How to Play:
•  Press `w` to move up

•  Press `s` to move down

•  Press `a` to move left

•  Press `d` to move right

•  Press `space` to exit


### Requirements:
None

### How to Run
Run the command: `python ./grid_base.py`
</div>
