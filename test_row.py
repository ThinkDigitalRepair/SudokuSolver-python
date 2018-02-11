from unittest import TestCase

from cell import Cell
from error import *
from row import Row


class TestRow(TestCase):
    def setUp(self):
        self.row = Row(0, [2, 1, 4, 3, 5, 7, 6, 9, 8])

    def test_sum(self):
        self.assertLessEqual(self.row.sum(), 45)

    def test_add_type_error(self):
        self.assertRaises(TypeError, self.row.add, 10)

    def test_add_value_error(self):
        self.assertRaises(ValueOutOfBoundsError, self.row.add, Cell(1, 2, 3))

    def test_set_cell(self):
        pass
