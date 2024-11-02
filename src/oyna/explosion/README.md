# [Dino or Dinosaur Game](https://en.wikipedia.org/wiki/Dinosaur_Game)

From Wikipedia, the free encyclopedia


The Dinosaur Game (also known as the Chrome Dino) is a browser game developed by Google and built into the Google Chrome web browser. The player guides a pixelated Tyrannosaurus rex across a side-scrolling landscape, avoiding obstacles to achieve a higher score. The game was created by members of the Chrome UX team in 2014.


## [Grid Base:](./grid_base.py)

<div style="text-align: justify;">


### How to Implement
This game is implemented as a grid table where elements are connected with their neighbors through links. When any button is pressed, the bird jumps and can pass through the cacti. To move cacti, the status of the cactus element is changed to `BLOCK` and the status of the left element is changed to `CACTUS`, If the cactus hits the bird, you lose.



<img align=right style="width:40%;" src="../../../docs/images/dino.png">


### How to Play:
•  Press `any key` to move up like `w` or `up arrow`


### Requirements:
`pynput`

### How to Run
Run the command: `python ./grid_base.py`
</div>
