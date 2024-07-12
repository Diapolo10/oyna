import enum


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
    EMPTY = " "
    PLAYER = "🟦"
    WALL = "🔹"
    END = "🟩"


class Action(enum.Enum):
    MOVE_DOWN = "down"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    MOVE_UP = "up"
    EXIT = "exit"


class Cell:
    def __init__(self, state: State = State.BLOCK) -> None:
        self.player_is_here: bool = False
        self.state: State = state
        self.seen: bool = False
        self.down: "Cell"
        self.up: "Cell"
        self.right: "Cell"
        self.left: "Cell"

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

    def take(self, action: Action) -> "Cell":
        match action:
            case Action.EXIT:
                self.state = State.END
                return self
            case _:
                return self.move_tile(action)

    def move_tile(self, action: Action) -> "Cell":
        side: "Cell" = getattr(self, action.value)
        if side.state == State.WALL:
            return self
        else:
            self.player_is_here = False
            side.player_is_here = True
            return side


class Board:
    def __init__(self, size: int) -> None:
        self.player: Cell
        self.size = size + 2
        self.cells: list[list[Cell]]
        self.set_initial()

    def set_initial(self) -> None:
        self.set_cells()
        self.set_walls()
        self.set_cells_neighboring()
        self.set_player()
        self.set_path()

    def set_cells(self):
        self.cells = [
            [Cell() for _ in range(self.size)] for _ in range(self.size)
        ]

    def set_walls(self) -> None:
        for i in range(self.size):
            for j in [0, self.size - 1]:
                self.cells[j][i].state = State.WALL
                self.cells[i][j].state = State.WALL

    def set_cells_neighboring(self) -> None:
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                self.cells[i][j].set_neighbors(
                    self.cells[i][j - 1],
                    self.cells[i][j + 1],
                    self.cells[i - 1][j],
                    self.cells[i + 1][j],
                )

    def set_player(self) -> None:
        self.player = self.cells[self.size // 2][self.size // 2]
        self.player.player_is_here = True

    def set_path(self) -> None:
        pass

    def take(self, ch: str):
        self.player = self.player.take(
            {
                "w": Action.MOVE_UP,
                "a": Action.MOVE_LEFT,
                "s": Action.MOVE_DOWN,
                "d": Action.MOVE_RIGHT,
                " ": Action.EXIT,
            }[ch]
        )

    def __str__(self) -> str:
        return "\n".join(["".join(map(str, rows)) for rows in self.cells])

    def player_has_reached_the_end(self):
        return self.player.state == State.END


class Game:
    def __init__(self):
        self.board = Board(20)

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
