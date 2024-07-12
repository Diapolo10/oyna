import enum
import itertools
import random
import typing

emojis = [
    "🧁",
    "🐣",
    "🍰",
    "🍨",
    "🦄",
    "🐝",
    "🍀",
    "🍹",
    "🍬",
    "🍁",
    "🍄",
    "🍇",
    "🍓",
    "🍥",
    "🍒",
    "🍭",
    "🍉",
    "🥗",
    "🧀",
    "🍩",
    "🌭",
    "🍌",
    "🥥",
    "🐢",
    "🍿",
    "🍕",
]


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


class State(enum.Enum):
    BLOCK = "🟪"
    WALL = "🔹"
    PLAYER = "🟦"
    SOLVED = "🔸"
    WIN = "🏆"
    EXIT = enum.auto()


class Side(enum.Enum):
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    UP = "up"


class Cell:
    def __init__(self, state: State = State.BLOCK) -> None:
        self.player_is_here = False
        self.state = state
        self.selected = False
        self.value = None
        self.down = None
        self.up = None
        self.right = None
        self.left = None

    def __str__(self) -> str:
        if self.selected:
            return self.value
        elif self.player_is_here:
            return State.PLAYER.value
        return self.state.value

    def set_neighbors(
        self, left: "Cell", right: "Cell", up: "Cell", down: "Cell"
    ) -> None:
        self.down = down
        self.up = up
        self.right = right
        self.left = left

    def set_value(self, value: str) -> None:
        self.value = value

    def set_selected(self, selected: bool) -> None:
        self.selected = selected

    def set_player_is_here(self, player_is_here: bool) -> None:
        self.player_is_here = player_is_here

    def set_state(self, state: State) -> None:
        self.state = state

    def move_tile(self, action: Side) -> "Cell":
        side_: "Cell" = getattr(self, action.value)
        if side_.state == State.WALL:
            return self
        else:
            self.player_is_here = False
            side_.player_is_here = True
            return side_


class Board:
    def __init__(self, size: int) -> None:
        self.start_player_position = size // 2
        self.size = size + (size % 2)
        self.cells = self._cells()
        self.set_initial()
        self.selected_tile: typing.Optional[Cell] = None
        self.player = self.cells[self.start_player_position][
            self.start_player_position
        ]

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
        self.set_cells_value()
        self.set_cells_neighboring()
        self.set_player()

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
        self.cells[self.start_player_position][
            self.start_player_position
        ].set_player_is_here(True)

    def set_cells_value(self) -> None:
        emoji_needs = divmod(pow(self.size, 2), 2 * len(emojis))
        complete_emojis = emojis * emoji_needs[0]
        extra_emojis = emojis[: emoji_needs[1] // 2]
        emojis_ = 2 * (complete_emojis + extra_emojis)
        random.shuffle(emojis_)
        emoji_cells = filter(
            lambda c: c.state != State.WALL, itertools.chain(*self.cells)
        )
        for i, cell in enumerate(emoji_cells):
            cell.set_value(emojis_[i])

    def action(self, ch: str) -> None:
        match ch:
            case "w":
                self.player = self.player.move_tile(Side.UP)
            case "a":
                self.player = self.player.move_tile(Side.LEFT)
            case "s":
                self.player = self.player.move_tile(Side.DOWN)
            case "d":
                self.player = self.player.move_tile(Side.RIGHT)
            case "e":
                if self.player.state != State.SOLVED:
                    if self.selected_tile:
                        if self._matched():
                            self._set_selected_tiles_as_solved()
                        else:
                            self._revert_selected_tile()
                    else:
                        self._select_new_tile()
            case " ":
                self.player.state = State.EXIT
            case _:
                pass

    def _select_new_tile(self) -> None:
        self.selected_tile = self.player
        self.selected_tile.set_selected(True)

    def _revert_selected_tile(self) -> None:
        self.selected_tile.set_selected(False)
        self._select_new_tile()

    def _set_selected_tiles_as_solved(self) -> None:
        if self.selected_tile:
            self.selected_tile.state = State.SOLVED
            self.player.state = State.SOLVED
            self.selected_tile.set_selected(False)
        self.selected_tile = None

    def _matched(self) -> bool:
        return (
            self.selected_tile.value == self.player.value
            and self.selected_tile != self.player
        )

    def __str__(self) -> str:
        return "\n".join(["".join(map(str, rows)) for rows in self.cells])

    def player_win(self) -> bool:
        for cell in itertools.chain(*self.cells):
            if cell.state != State.SOLVED and cell.state != State.WALL:
                return False
        self.player.set_state(State.WIN)
        return True


class Game:
    def __init__(self) -> None:
        self.board = Board(8)

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
            not self.board.player_win()
            and self.board.player.state != State.EXIT
        )

    def print_result(self) -> None:
        self._print_board()


if __name__ == "__main__":
    Game().run()
