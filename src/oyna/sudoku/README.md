# Sudoku


# [Sudoku](https://en.wikipedia.org/wiki/Sudoku)

From Wikipedia, the free encyclopedia

Sudoku (/suːˈdoʊkuː, -ˈdɒk-, sə-/; Japanese: 数独, romanized: sūdoku, lit. 'digit-single'; originally called Number Place)[1] is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contains all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

French newspapers featured variations of the Sudoku puzzles in the 19th century, and the puzzle has appeared since 1979 in puzzle books under the name Number Place. However, the modern Sudoku only began to gain widespread popularity in 1986 when it was published by the Japanese puzzle company Nikoli under the name Sudoku, meaning "single number". It first appeared in a U.S. newspaper, and then The Times (London), in 2004, thanks to the efforts of Wayne Gould, who devised a computer program to rapidly produce unique puzzles.



## [Grid Base:](./grid_base.py)

<div style="text-align: justify;">


### How to Implement
This game is implemented as a grid table where elements are connected with their neighbors through links. Each element of this table contains a `Cell`, Each `Cell` has different states, based on which the state of the number or character is displayed.
Based on the [alain-t method](https://stackoverflow.com/a/56581709/8157102), a sudoku table is created and several cell are randomly hidden and the user must enter them to solve the sudoku.


<img align=right style="width:40%;" src="../../../docs/images/sudoku.png">


### How to Play:
•  Press `w` to move up

•  Press `s` to move down

•  Press `a` to move left

•  Press `d` to move right

•  Press `1`-`9` to insert numbers

•  Press `space` to exit


### Requirements:
None

### How to Run
Run the command: `python ./grid_base.py`
</div>
