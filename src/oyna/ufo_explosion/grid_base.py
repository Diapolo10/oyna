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


class Board:
    def __init__(self, height: int) -> None:
        self.height, self.length = height, height // 2 * 10
        self.cells: list[list[str]] = self._cells()
        self.player = -2, 1
        self.cells[self.player[0]][self.player[1]] = "🛸"
        self.create_castle()

    def _cells(self) -> list[list[str]]:
        return [
            [
                "🔹" if j in [0, self.length - 1] or i in [0, self.height - 1] else "  "
                for j in range(self.length)
            ]
            for i in range(self.height)
        ]

    def action(self, character: str) -> None:
        if character.isdigit():
            self.move(int(character) * self.height // 2)
        else:
            exit()

    def move(self, step: int) -> None:
        for i in range(step):
            self.cells[self.player[0]][self.player[1]] = "  "

            if i < self.height - 3 and i < step // 2:
                self.player = self.player[0] - 1, self.player[1] + 1
            elif i >= (step + 1) // 2 and step - i < self.height - 2:
                self.player = self.player[0] + 1, self.player[1] + 1
            else:
                self.player = self.player[0], self.player[1] + 1
            self.cells[self.player[0]][self.player[1]] = "🛸"
            print(self)
            sleep(0.05)
        self._boom()

    def _boom(self) -> None:
        for i in range((self.height + 1) // 2):
            self.cells[self.player[0]][self.player[1] - i] = "💥"
        print(self)
        sleep(0.3)
        for i in range((self.height + 1) // 2):
            self.cells[self.player[0]][self.player[1] - i] = "  "
        self.player = self.height - 2, 1
        self.cells[self.player[0]][self.player[1]] = "🛸"
        self.create_castle()
        print(self)

    def create_castle(self) -> None:
        for cell in self.cells[-2]:
            if cell == "🏠":
                break
        else:
            self.cells[self.height - 2][
                random.randint(self.height // 2, self.length - 2)
            ] = "🏠"

    def __str__(self) -> str:
        return "\033[H\033[J" + "\n".join(
            ["".join([str(cell) for cell in rows]) for rows in self.cells]
        )


def run() -> None:
    board = Board(15)
    print(board)

    while True:
        board.action(getch())


if __name__ == "__main__":
    run()
