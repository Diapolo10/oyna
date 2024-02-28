import itertools
import math
import unittest

from src.poxly.main import Board, State


class BoardTestCase(unittest.TestCase):
    def test_board_size(self) -> None:
        board = Board(20)
        self.assertEqual(len(board.cells), 22)
        self.assertEqual(len(board.cells[0]), 44)
        self.assertEqual(board.height, 22)
        self.assertEqual(board.width, 44)

    def test_board_items(self) -> None:
        board = Board(20)
        enemy = ball = wall = ant = stair = 0
        for cell in itertools.chain(*board.cells):
            enemy += cell.state == State.ENEMY
            ball += cell.state == State.BALL
            wall += cell.state == State.WALL
            ant += cell.state == State.ANT
            stair += cell.state == State.STAIR

        self.assertEqual(1, enemy)
        self.assertEqual(1, ball)
        self.assertEqual(128, wall)
        self.assertEqual(0, ant)
        self.assertTrue(math.isclose(28, stair, abs_tol=2))
