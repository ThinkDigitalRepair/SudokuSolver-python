from cell import Cell
from error import *


class Row(list):

    def __init__(self, row_number, cells):

        assert (isinstance(row_number, int))
        assert (isinstance(cells, list))

        self.row_number = row_number

        for column, value in enumerate(cells):
            cell = Cell(column=column, row=row_number, value=value)
            self.add(cell)

        self.solved = False if self.sum() == 45 else True

    def add(self, cell):
        # make sure cell is a cell
        # make sure cell doesn't already exist in this row,
        # that it's not putting us over our limit (Both should never happen)
        # that it's within the range of acceptable values
        if not isinstance(cell, Cell):
            raise TypeError("Expecting {0}, got {1}".format(Cell, type(cell)))

        elif cell in self:
            raise ValueError("{0} is already present at position {1}".format(cell, self.index(cell)))

        elif self.sum() + cell > 45:
            raise ValueOutOfBoundsError(cell)

        elif cell.value not in range(0, 9 + 1):
            raise ValueOutOfBoundsError(cell)

        self.append(cell)

    def sum(self):
        return sum(self)
