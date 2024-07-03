# # we use https://stackoverflow.com/a/56581709/8157102 solution written by https://stackoverflow.com/users/5237560/alain-t

import enum
import math
import random
from random import sample
from typing import Optional


def getch():
    """Gets a single character"""
    try:
        import msvcrt

        return msvcrt.getch().decode("utf-8")
    except ImportError:
        import sys
        import termios
        import tty

        fd = sys.stdin.fileno()
        oldsettings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldsettings)
        return ch


class State(enum.Enum):
    BLOCK = "🟪"
    EMPTY = "  "
    PLAYER = "🟦"
    INTERNAL_WALL = "🔹"
    EXTERNAL_WALL = "🔸"
    FIXED_NUMBER = ""
    END = "🟩"


class Action(enum.Enum):
    MOVE_DOWN = "down"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    MOVE_UP = "up"
    EXIT = "exit"
    NOTHING = "nothing"
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class Color:
    CORRECT = "\033[92m"
    ERROR = "\033[91m"
    NORMAL = "\033[0m"


class Cell:
    def __init__(self, state: State = State.BLOCK, value: int = -1) -> None:
        self.player_is_here: bool = False
        self.state: State = state
        self.seen: bool = False
        self.value: int = value
        self.user_value: Optional[int] = None
        self.down: "Cell"
        self.up: "Cell"
        self.right: "Cell"
        self.left: "Cell"

    def __str__(self) -> str:
        if self.player_is_here:
            return State.PLAYER.value
        elif self.state == State.FIXED_NUMBER:
            return f"{self.value:2}"
        elif self.state == State.EMPTY:
            if self.user_value:
                color = Color.CORRECT if self.value == self.user_value else Color.ERROR
                return f"{color}{self.user_value:2}{Color.NORMAL}"
            return str(self.state.value)

        else:
            return str(self.state.value)

    def set_neighbors(
        self, left: "Cell", right: "Cell", up: "Cell", down: "Cell"
    ) -> None:
        self.down = down
        self.up = up
        self.right = right
        self.left = left

    def take(self, action: Action) -> "Cell":
        match action:
            case Action.EXIT:
                self.state = State.END
                return self

            case move if move in [
                Action.MOVE_DOWN,
                Action.MOVE_RIGHT,
                Action.MOVE_UP,
                Action.MOVE_LEFT,
            ]:
                return self.move_tile(move)
            case Action.NOTHING:
                return self
            case _:
                return self.enter(action)

    def enter(self, action) -> "Cell":
        if self.state == State.EMPTY:
            self.user_value = action.value
        return self

    def move_tile(self, action: Action) -> "Cell":
        side: "Cell" = getattr(self, action.value)
        if side.state == State.EXTERNAL_WALL:
            return self
        elif side.state == State.INTERNAL_WALL:
            side_side: "Cell" = getattr(side, action.value)
            side_side.player_is_here = True
            self.player_is_here = False
            return side_side
        else:
            self.player_is_here = False
            side.player_is_here = True
            return side


class Board:
    def __init__(self) -> None:
        self.size = 3
        self.player: Cell
        self.line_size = self.size**2 + self.size + 1
        self.cells: list[list[Cell]]
        self.set_initial()

    def set_initial(self) -> None:
        self.set_cells()
        self.set_walls()
        self.set_cells_neighboring()
        self.set_numbers()
        self.set_empty_cells()
        self.set_player()

    def set_cells(self):
        self.cells = [
            [Cell() for _ in range(self.line_size)] for _ in range(self.line_size)
        ]

    def set_walls(self) -> None:
        for i in range(self.line_size - 1):
            for j in [0, self.line_size - 1]:
                self.cells[i][j].state = State.EXTERNAL_WALL
                self.cells[j][i].state = State.EXTERNAL_WALL

            for j in range(self.size + 1, self.line_size - self.size, self.size + 1):
                self.cells[i][j].state = State.INTERNAL_WALL
                self.cells[j][i].state = State.INTERNAL_WALL

        self.cells[self.line_size - 1][self.line_size - 1].state = State.EXTERNAL_WALL

    def set_cells_neighboring(self) -> None:
        for i in range(1, self.line_size - 1):
            for j in range(1, self.line_size - 1):
                self.cells[i][j].set_neighbors(
                    self.cells[i][j - 1],
                    self.cells[i][j + 1],
                    self.cells[i - 1][j],
                    self.cells[i + 1][j],
                )

    def set_player(self) -> None:
        self.player = self.cells[1][1]
        self.player.player_is_here = True

    def set_numbers(self):
        side = self.size * self.size

        def pattern(r, c):
            return (self.size * (r % self.size) + r // self.size + c) % side

        def shuffle(s):
            return sample(s, len(s))

        rBase = range(self.size)
        rows = [g * self.size + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * self.size + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, self.size * self.size + 1))

        numbers = [[nums[pattern(r, c)] for c in cols] for r in rows]
        for i, row in enumerate(numbers):
            for j, value in enumerate(row):
                i_ = i + math.floor(i / self.size) + 1
                j_ = j + math.floor(j / self.size) + 1
                self.cells[i_][j_].value = value
                self.cells[i_][j_].state = State.FIXED_NUMBER

    def set_empty_cells(self):
        for row in self.cells:
            for cell in row:
                cell.state = (
                    State.EMPTY
                    if cell.state == State.FIXED_NUMBER and random.randint(0, 7) > 2
                    else cell.state
                )

    def take(self, ch: str):
        print(ch)
        self.player = self.player.take(
            {
                "w": Action.MOVE_UP,
                "a": Action.MOVE_LEFT,
                "s": Action.MOVE_DOWN,
                "d": Action.MOVE_RIGHT,
                " ": Action.EXIT,
                "1": Action.ONE,
                "2": Action.TWO,
                "3": Action.THREE,
                "4": Action.FOUR,
                "5": Action.FIVE,
                "6": Action.SIX,
                "7": Action.SEVEN,
                "8": Action.EIGHT,
                "9": Action.NINE,
            }.get(ch, Action.NOTHING)
        )

    def __str__(self) -> str:
        return "\n".join(["".join(map(str, rows)) for rows in self.cells])

    def player_has_reached_the_end(self):
        return self.player.state == State.END


class Game:
    def __init__(self):
        self.board = Board()

    def run(self) -> None:
        while not self.board.player_has_reached_the_end():
            self.print_board()
            self.board.take(getch())
            self.print_board()

    @staticmethod
    def clear_screen():
        print("\033[H\033[J", end="")

    def print_board(self):
        self.clear_screen()
        print(self.board)


if __name__ == "__main__":
    Game().run()
