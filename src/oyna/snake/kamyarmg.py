import enum
import random
from dataclasses import dataclass
from time import sleep
from typing import Optional

from pynput import keyboard


class State(enum.Enum):
    BLOCK = "  "
    APPLE = "🍎"
    WALL = "🔹"
    PLAYER = "🟪"
    HEAD = "🟨"
    END = "  "


class Direction(enum.Enum):
    LEFT = "left"
    RIGHT = "right"
    DOWN = "down"
    UP = "up"


@dataclass
class UserInput:
    value: Optional[Direction] = None


user_input = UserInput()


def set_user_input(key: Optional[keyboard.KeyCode | keyboard.Key]) -> None:
    key_ = key.char if isinstance(key, keyboard.KeyCode) else "d"
    match key_:
        case "d":
            user_input.value = (
                Direction.RIGHT
                if user_input.value != Direction.LEFT
                else user_input.value
            )
        case "a":
            user_input.value = (
                Direction.LEFT
                if user_input.value != Direction.RIGHT
                else user_input.value
            )
        case "w":
            user_input.value = (
                Direction.UP
                if user_input.value != Direction.DOWN
                else user_input.value
            )
        case "s":
            user_input.value = (
                Direction.DOWN
                if user_input.value != Direction.UP
                else user_input.value
            )
        case _:
            pass


class Cell:
    def __init__(self, state: State = State.BLOCK) -> None:
        self.direction: Optional[Direction] = None
        self.state = state
        self.previous_cell: Optional["Cell"] = None
        self.down: "Cell"
        self.up: "Cell"
        self.right: "Cell"
        self.left: "Cell"

    def __str__(self) -> str:
        return str(self.state.value)


class Board:
    def __init__(self, size: int) -> None:
        self.head: Cell
        self.size = size + 2
        self.cells = [
            [Cell() for _ in range(self.size)] for _ in range(self.size)
        ]
        self.set_walls()
        self.set_cells_neighboring()
        self.set_player()
        self.set_apple()

    def set_walls(self) -> None:
        for i in range(self.size):
            for j in [0, self.size - 1]:
                self.cells[j][i].state = State.WALL
                self.cells[i][j].state = State.WALL

    def set_apple(self) -> None:
        random.choice(
            [
                cell
                for row in self.cells
                for cell in row
                if cell.state == State.BLOCK
            ]
        ).state = State.APPLE

    def set_cells_neighboring(self) -> None:
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                self.cells[i][j].left = self.cells[i][j - 1]
                self.cells[i][j].right = self.cells[i][j + 1]
                self.cells[i][j].up = self.cells[i - 1][j]
                self.cells[i][j].down = self.cells[i + 1][j]

    def set_player(self) -> None:
        body = self.cells[self.size // 2][self.size // 2 - 1]
        body.state = State.PLAYER
        self.head = self.cells[self.size // 2][self.size // 2]
        self.head.previous_cell = body
        self.head.state = State.HEAD

    def move(self) -> None:
        if user_input.value is not None:
            cell = getattr(self.head, user_input.value.value)
            if cell.state in [State.WALL, State.PLAYER]:
                self.head.state = State.END
            elif cell.state == State.APPLE:
                cell.state = State.HEAD
                cell.direction = user_input.value
                cell.previous_cell = self.head
                self.head.state = State.PLAYER
                self.head = cell
                self.set_apple()
            else:
                cell.direction = user_input.value
                cell.previous_cell = self.head
                self.head = cell
                self._move(self.head)

    def _move(self, cell: Optional[Cell]) -> None:
        if cell is not None:
            if (
                cell.previous_cell is not None
                and cell.previous_cell.state != State.BLOCK
            ):
                cell.state = cell.previous_cell.state
                self._move(cell.previous_cell)
            else:
                cell.state = State.BLOCK
                cell.direction = None

    def __str__(self) -> str:
        return "\n".join(
            ["".join([str(cell) for cell in rows]) for rows in self.cells]
        )


class Game:
    def __init__(self) -> None:
        self.board = Board(20)

    def run(self) -> None:
        listener = keyboard.Listener(on_press=set_user_input)
        listener.start()
        while self.board.head.state != State.END:
            print("\033[H\033[J")
            print(self.board)
            sleep(0.08)
            self.board.move()


if __name__ == "__main__":
    Game().run()
