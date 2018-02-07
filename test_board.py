from unittest import TestCase
from board import Board


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board("Easy Puzzle1.set")

    def test_box(self):
        box0 = self.board.get_box(0)
        box1 = self.board.get_box(1)
        box2 = self.board.get_box(2)
        box3 = self.board.get_box(3)
        box4 = self.board.get_box(4)
        box5 = self.board.get_box(5)
        pass
