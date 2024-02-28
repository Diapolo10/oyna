from enum import Enum, auto
import random
import typing
from pynput import keyboard


class Image(Enum):
    BALL = "💩"
    ENEMY = "🗿"
    ANT = "🐝"
    STAIR = "➖"
    EMPTY = "  "
    WALL = "🔳"
    BLADE = "🔱"


class State(Enum):
    BALL = auto()
    ENEMY = auto()
    ANT = auto()
    EMPTY = auto()
    STAIR = auto()
    WIN = auto()
    FAILED = auto()
    WALL = auto()
    BLADE = auto()


class Cell:
    def __init__(
        self,
        state: State = State.EMPTY,
        left: typing.Optional["Cell"] = None,
        right: typing.Optional["Cell"] = None,
        top: typing.Optional["Cell"] = None,
        bottom: typing.Optional["Cell"] = None,
    ) -> None:
        self._state = state
        self._self = left
        self._right = right
        self._top = top
        self._bottom = bottom

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, value: State) -> None:
        self._state = value

    def __str__(self) -> str:
        match self.state:
            case State.BALL:
                return Image.BALL.value
            case State.ENEMY:
                return Image.ENEMY.value
            case State.STAIR:
                return Image.STAIR.value
            case State.ANT:
                return Image.ANT.value
            case State.WALL:
                return Image.WALL.value
            case State.BLADE:
                return Image.BLADE.value
            case _:
                return Image.EMPTY.value

    def set_neighbors(self, left: "Cell", right: "Cell", top: "Cell", bottom: "Cell") -> None:
        self._bottom = bottom
        self._top = top
        self._right = right
        self._left = left


class Board:
    def __init__(self, size: int) -> None:
        self._size = size
        self.cells = self._cells()
        self._set_initial()

    def _cells(self) -> list[list[Cell]]:
        return [[Cell() for _ in range(self.width)] for _ in range(self.height)]

    @property
    def height(self) -> int:
        return self._size + 2

    @property
    def width(self) -> int:
        return 2 * (self._size + 2)

    def _set_initial(self) -> None:
        self._set_horizontal_walls()
        self._set_vertical_walls()
        self._set_cells_neighboring()
        self._set_ball()
        self._set_stairs()
        self._set_enemy()
        self._set_blade()

    def _set_ball(self) -> None:
        self.cells[self.height - 2][1].state = State.BALL

    def _set_cells_neighboring(self) -> None:
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                self.cells[i][j].set_neighbors(
                    self.cells[i][j - 1],
                    self.cells[i][j + 1],
                    self.cells[i - 1][j],
                    self.cells[i + 1][j],
                )

    def _set_vertical_walls(self) -> None:
        for i in range(self.height):
            self.cells[i][0].state = State.WALL
            self.cells[i][self.width - 1].state = State.WALL

    def _set_horizontal_walls(self) -> None:
        for j in range(self.width):
            self.cells[0][j].state = State.WALL
            self.cells[self.height - 1][j].state = State.WALL

    def _set_stairs(self) -> None:
        for _ in range(1, int(self._size * 1.5)):
            i = self._get_random_index(self.height)
            j = self._get_random_index(self.width)
            self.cells[i][j].state = State.STAIR

    def _set_enemy(self) -> None:
        self.cells[5][self.width - 2].state = State.ENEMY

    def _set_blade(self) -> None:
        for _ in range(4):
            i = self.height - 2
            j = self._get_random_index(self.width - 1, 10)
            self.cells[i][j].state = State.BLADE

    def _get_random_index(self, end: int, stairs_const: int = 4) -> int:
        return random.randint(stairs_const, end - stairs_const)

    def __str__(self) -> str:
        return "\n".join(["".join([str(cell) for cell in rows]) for rows in self.cells])

    def clear_screen(self):
        print("\033[H\033[J", end="")


class Game:
    def __init__(self, size: int = 30) -> None:
        self.board = Board(size)

    def on_press(self, key: keyboard.Key) -> None:
        match key:
            case keyboard.Key.up:
                pass
            case keyboard.Key.down:
                pass
            case keyboard.Key.left:
                pass
            case keyboard.Key.right:
                pass
            case _:
                pass

    def on_release(self, key: keyboard.Key) -> typing.Literal[False] | None:
        pass

    def run(self) -> None:
        keyboard.Listener(on_press=self.on_press, on_release=self.on_release).start()


if __name__ == "__main__":
    # Game(30).run()
    print(Board(30))
