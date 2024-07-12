import enum
import random
from math import ceil
from typing import Optional


def getch() -> str:
    """Gets a single character"""
    try:
        import msvcrt

        return str(msvcrt.getch().decode("utf-8"))
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


selected_emoji = random.choice(
    [
        ("😀", "😄"),
        ("😄", "😁"),
        ("😙", "😗"),
        ("🈹", "🈵"),
        ("🙂", "🙃"),
        ("😏", "😒"),
        ("😈", "👿"),
        ("🧒", "👨"),
        ("🌔", "🌖"),
        ("😅", "🥲"),
        ("🤪", "😜"),
        ("🌍", "🌏"),
        ("🤩", "😍"),
        ("😺", "😻"),
        ("🥇", "🏅"),
        ("😳", "🙄"),
        ("🕐", "🕚"),
    ]
)


class State(enum.Enum):
    BLOCK = selected_emoji[0]
    ANSWER = selected_emoji[1]
    INCORRECT_ANSWER = "🟥"
    PLAYER = "🟩"
    WALL = "🍀"
    WIN = "🏆"
    EXIT = "🟩"


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
        self.down: Optional["Cell"] = None
        self.up: Optional["Cell"] = None
        self.right: Optional["Cell"] = None
        self.left: Optional["Cell"] = None

    def __str__(self) -> str:
        return str(
            State.PLAYER.value if self.player_is_here else self.state.value
        )

    def set_neighbors(
        self, left: "Cell", right: "Cell", up: "Cell", down: "Cell"
    ) -> None:
        self.down = down
        self.up = up
        self.right = right
        self.left = left

    def process(self, action: Action) -> "Cell":
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
        side: "Cell" = getattr(self, action.value)
        if side.state == State.WALL:
            return self
        else:
            self.player_is_here, side.player_is_here = (
                side.player_is_here,
                self.player_is_here,
            )
            return side

    def _click(self) -> None:
        self.state = State.WIN if self._correct() else State.INCORRECT_ANSWER

    def _correct(self) -> bool:
        return self.state == State.ANSWER


class Board:
    def __init__(self, size: int) -> None:
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
        self.set_walls()
        self.set_cells_neighboring()
        self.set_player()
        self.set_answer()

    def set_walls(self) -> None:
        for i in range(self.main_size):
            for j in [0, self.main_size - 1]:
                self.cells[j][i].state = State.WALL
                self.cells[i][j].state = State.WALL

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
        self.player.player_is_here = True

    def set_answer(self) -> None:
        i = random.randint(1, self.size)
        j = random.randint(1, self.size)
        self.cells[i][j].state = State.ANSWER

    def action(self, ch: str) -> None:
        match ch:
            case "w":
                self.player = self.player.process(Action.MOVE_UP)
            case "a":
                self.player = self.player.process(Action.MOVE_LEFT)
            case "s":
                self.player = self.player.process(Action.MOVE_DOWN)
            case "d":
                self.player = self.player.process(Action.MOVE_RIGHT)
            case "e":
                self.player = self.player.process(Action.CLICK)
            case " ":
                self.player = self.player.process(Action.EXIT)
            case _:
                pass

    def __str__(self) -> str:
        return "\n".join(
            ["".join([str(cell) for cell in rows]) for rows in self.cells]
        )

    def player_win(self) -> bool:
        return self.player.state == State.WIN


class Game:
    def __init__(self) -> None:
        self.board = Board(10)

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
        self.board.player.player_is_here = False
        self._print_board()


if __name__ == "__main__":
    Game().run()
