from unittest import TestCase

from board import Board
from cell import Cell


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board("Easy Puzzle1.set")

    def test_box(self):
        pass

    def test_update_possible_values(self):
        # self.board.update_possible_values()
        pass

    def test_cell_equality(self):
        self.assertTrue(self, Cell(1, 2, 3) == 3)

    def test_cell_equality_fails(self):
        pass
