from unittest import TestCase

from board import Board


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board("Easy Puzzle1.set")

    def test_box(self):
        pass
