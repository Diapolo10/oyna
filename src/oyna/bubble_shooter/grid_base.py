import enum
import random
from dataclasses import dataclass
from time import sleep
from typing import Literal, Optional

from pynput import keyboard


class State(enum.Enum):
    EMPTY = "  "
    WALL = "🔹"
    END = "💥"
    COLOR_RED = "🔴"
    COLOR_YELLOW = "🟡"
    COLOR_BLUE = "🔵"
    COLOR_WHITE = "⚪️"


def colors_state() -> list[State]:
    return [state for state in State if state.name.startswith("COLOR")]


class Action(enum.Enum):
    LEFT = "left"
    RIGHT = "right"
    CHANGE = "change"
    FIRE = "fire"


@dataclass
class UserInput:
    value: Optional[Action] = None


user_input = UserInput()


def set_user_input(key: Optional[keyboard.KeyCode | keyboard.Key]) -> None:
    key_ = key.char if isinstance(key, keyboard.KeyCode) else "d"
    match key_:
        case key_ if user_input.value is not None:
            user_input.value = None
        case "d":
            user_input.value = Action.RIGHT
        case "a":
            user_input.value = Action.LEFT
        case "w":
            user_input.value = Action.FIRE
        case "s":
            user_input.value = Action.CHANGE
        case _:
            pass


class Cell:
    def __init__(self, state: State = State.EMPTY) -> None:
        self.state: State = state
        self.down: "Cell"
        self.up: "Cell"
        self.right: "Cell"
        self.left: "Cell"

    def __str__(self) -> str:
        return str(self.state.value)


class Board:
    def __init__(self, size: int) -> None:
        self.player: Cell
        self.size = size + 2
        self.cells = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.set_walls()
        self.set_cells_neighboring()
        self.set_bubbles()
        self.set_player()

    def set_walls(self) -> None:
        for i in range(self.size):
            for j in [0, self.size - 1]:
                self.cells[i][j].state = State.WALL
                self.cells[j][i].state = State.WALL

    def set_cells_neighboring(self) -> None:
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                self.cells[i][j].left = self.cells[i][j - 1]
                self.cells[i][j].right = self.cells[i][j + 1]
                self.cells[i][j].up = self.cells[i - 1][j]
                self.cells[i][j].down = self.cells[i + 1][j]

    def set_player(self) -> None:
        self.player = self.cells[self.size - 2][self.size // 2]
        self.player.state = random.choice(colors_state())

    def set_bubbles(self) -> None:
        for row in self.cells[1 : self.size // 5]:
            for cell in row[1:-1]:
                cell.state = random.choice(colors_state())

    def update(self, step: int) -> None:
        match user_input.value:
            case Action.LEFT:
                self._move("left")
            case Action.RIGHT:
                self._move("right")
            case Action.FIRE:
                shooter = self.player
                while shooter.up.state == State.EMPTY:
                    shooter.up.state = shooter.state
                    shooter.state = State.EMPTY
                    shooter = shooter.up
                if self._matched(shooter):
                    self._clean_bubbles(shooter)
                self.player.state = random.choice(colors_state())

            case Action.CHANGE:
                self._change_player_color()
            case _:
                pass
        self._create_new_bubbles(step)
        self._clear_zombie_cells()

    def _change_player_color(self) -> None:
        self.player.state = random.choice(colors_state())

    def _move(self, side: Literal["left", "right"]) -> None:
        if getattr(self.player, side).state != State.WALL:
            getattr(self.player, side).state = self.player.state
            self.player.state = State.EMPTY
            self.player = getattr(self.player, side)

    def _create_new_bubbles(self, step: int) -> None:
        if step % (self.size**2) == 0:
            self._pull_down(1)

            for cell in self.cells[1][1:-1]:
                cell.state = random.choice(colors_state())

    def _clear_zombie_cells(self) -> None:
        for row in self.cells[1:-1]:
            for cell in row[1:-1]:
                cell.state = (
                    State.EMPTY
                    if cell != self.player and cell.up.state == State.EMPTY
                    else cell.state
                )

    def _pull_down(self, row_index: int) -> None:
        if row_index == self.size - 3:
            self.player.state = (
                State.END
                if any(cell.state in colors_state() for cell in self.cells[row_index])
                else self.player.state
            )
        else:
            self._pull_down(row_index + 1)
            for cell in self.cells[row_index][1:-1]:
                cell.down.state = cell.state

    def _clean_bubbles(self, cell: Cell) -> None:
        pr = cell.state
        cell.state = State.EMPTY

        for direction in ["left", "right", "up", "down"]:
            if (
                getattr(cell, direction) != cell
                and getattr(cell, direction).state == pr
            ):
                self._clean_bubbles(getattr(cell, direction))

    def _matched(self, cell: Cell) -> bool:
        is_matched: bool = (
            sum(
                [
                    cell.left.state == cell.state,
                    cell.right.state == cell.state,
                    cell.up.state == cell.state,
                    *[
                        getattr(cell, d).state != State.WALL
                        and getattr(getattr(cell, d), d2).state == cell.state
                        for d in ["left", "right", "up"]
                        for d2 in ["left", "down", "right", "up"]
                    ],
                ]
            )
            > 3
        )
        return is_matched

    def __str__(self) -> str:
        return "\n".join(["".join([str(cell) for cell in rows]) for rows in self.cells])


def run() -> None:
    listener = keyboard.Listener(on_press=set_user_input)
    listener.start()
    board = Board(15)
    step = 0
    while board.player.state != State.END:
        sleep(0.03)
        board.update(step)
        user_input.value = None
        print(f"\033[H\033[J{board}\nScores: {step // 33}")
        step += 1


if __name__ == "__main__":
    run()
