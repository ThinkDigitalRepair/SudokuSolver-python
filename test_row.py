from unittest import TestCase

from cell import Cell
from row import Row


class TestRow(TestCase):
    def setUp(self):
        self.row = Row(0, [2, 0, 4, 3, 5, 0, 6, 9, 8])

    def test_sum(self):
        self.assertLessEqual(self.row.sum(), 45)

    def test_add_type_error(self):
        self.assertRaises(TypeError, self.row.add, 10)

    def test_add_value_error(self):
        self.assertRaises(ValueError, self.row.add, Cell(1, 2, 3))

    def test_set_cell(self):
        pass

    def test_updating_row_values(self):
        self.row.set_cell(1, 1)
        pass
