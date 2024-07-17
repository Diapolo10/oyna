import enum
import random
from time import sleep


def getch() -> str:
    """Gets a single character"""
    try:
        import msvcrt

        return str(msvcrt.getch().decode("utf-8"))  # type: ignore
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
    BLOCK_PREVIEW = "🟩"
    CORRECT_ANSWER = "✅"
    INCORRECT_ANSWER = "🟥"
    PLAYER = "🟦"
    WALL = "🔹"
    WIN = "🏆"
    EXIT = ""


class Action(enum.Enum):
    CLICK = "click"
    MOVE_DOWN = "down"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    MOVE_UP = "up"
    EXIT = "exit"


class Cell:
    def __init__(self, state: State = State.BLOCK) -> None:
        self.player_is_here = False
        self.state = state
        self.value = 0
        self.down: "Cell"
        self.up: "Cell"
        self.right: "Cell"
        self.left: "Cell"

    def __str__(self) -> str:
        return (
            State.PLAYER.value
            if self.player_is_here
            else str(self.state.value)
        )

    def set_neighbors(
        self, left: "Cell", right: "Cell", up: "Cell", down: "Cell"
    ) -> None:
        self.down = down
        self.up = up
        self.right = right
        self.left = left

    def set_state(self, action: Action) -> "Cell":
        match action:
            case Action.CLICK:
                self._click()
                return self
            case Action.EXIT:
                self.state = State.EXIT
                return self
            case _:
                return self._move_tile(action)

    def _move_tile(self, action: Action) -> "Cell":
        side_: "Cell" = getattr(self, action.value)
        if side_.state == State.WALL:
            return self
        else:
            self.player_is_here, side_.player_is_here = (
                side_.player_is_here,
                self.player_is_here,
            )
            return side_

    def _click(self) -> None:
        self.state = (
            State.CORRECT_ANSWER if self._correct() else State.INCORRECT_ANSWER
        )

    def _correct(self) -> bool:
        return self.value > 0


class Board:
    def __init__(self, size: int) -> None:
        self.blocks: list[Cell] = []
        self.player: Cell
        self.size = size
        self.cells = self._cells()
        self.set_initial()

    def _cells(self) -> list[list[Cell]]:
        return [
            [Cell() for _ in range(self.main_size)]
            for _ in range(self.main_size)
        ]

    @property
    def main_size(self) -> int:
        return self.size + 2

    def set_initial(self) -> None:
        self.set_horizontal_walls()
        self.set_vertical_walls()
        self.set_cells_neighboring()
        self.set_player()
        self.set_blocks()

    def set_horizontal_walls(self) -> None:
        for j in range(self.main_size):
            self.cells[0][j].state = State.WALL
            self.cells[self.main_size - 1][j].state = State.WALL

    def set_vertical_walls(self) -> None:
        for i in range(self.main_size):
            self.cells[i][0].state = State.WALL
            self.cells[i][self.main_size - 1].state = State.WALL

    def set_cells_neighboring(self) -> None:
        for i in range(1, self.main_size - 1):
            for j in range(1, self.main_size - 1):
                self.cells[i][j].set_neighbors(
                    self.cells[i][j - 1],
                    self.cells[i][j + 1],
                    self.cells[i - 1][j],
                    self.cells[i + 1][j],
                )

    def set_player(self) -> None:
        self.player = self.cells[self.main_size // 2][self.main_size // 2]

    def set_blocks(self) -> None:
        for _ in range(self.size // 2):
            block = self.cells[random.randint(2, self.size - 1)][
                random.randint(2, self.size - 1)
            ]
            block.value = 1
            block.state = State.BLOCK_PREVIEW
            self.blocks.append(block)

    def action(self, ch: str) -> None:
        match ch:
            case "w":
                self.player = self.player.set_state(Action.MOVE_UP)
            case "a":
                self.player = self.player.set_state(Action.MOVE_LEFT)
            case "s":
                self.player = self.player.set_state(Action.MOVE_DOWN)
            case "d":
                self.player = self.player.set_state(Action.MOVE_RIGHT)
            case "e":
                self.player = self.player.set_state(Action.CLICK)
            case " ":
                self.player = self.player.set_state(Action.EXIT)
            case _:
                pass

    def __str__(self) -> str:
        return "\n".join(
            ["".join([str(cell) for cell in rows]) for rows in self.cells]
        )

    def player_win(self) -> bool:
        for cell in self.blocks:
            if cell.state != State.CORRECT_ANSWER:
                return False
        return True

    def preview(self) -> None:
        print(self)
        sleep(3)
        self.player.player_is_here = True
        for block in self.blocks:
            block.state = State.BLOCK


class Game:
    def __init__(self) -> None:
        self.board = Board(15)
        self.board.preview()

    def run(self) -> None:
        while self.allow_continue():
            self._print_board()
            self.board.action(getch())
        self.print_result()

    @staticmethod
    def clear_screen() -> None:
        print("\033[H\033[J", end="")

    def _print_board(self) -> None:
        self.clear_screen()
        print(self.board)

    def allow_continue(self) -> bool:
        return (
            self.board.player.state != State.EXIT
            and not self.board.player_win()
        )

    def print_result(self) -> None:
        self.player_is_here = False
        self._print_board()


if __name__ == "__main__":
    Game().run()
