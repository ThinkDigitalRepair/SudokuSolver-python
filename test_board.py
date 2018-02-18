from unittest import TestCase

from board import Board
from cell import Cell


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board("Medium1.set")

    def test_box(self):
        pass

    def test_update_possible_values(self):
        # self.board.update_possible_values()
        pass

    def test_cell_equality(self):
        self.assertTrue(self, Cell(1, 2, 3) == 3)

    def test_cell_equality_fails(self):
        pass

    def test_ordered_by_completeness(self):
        a = self.board.ordered_by_completeness

    def test_solve(self):
        self.board.solve()
        self.board.__print__()
        pass

    def test_percent_complete(self):
        board_completeness = self.board.percent_complete
        print("board completeness: " + str(board_completeness) + '%')
        self.board.__print__()
