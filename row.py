from cell import Cell
from error import *


class Row(list):

    def __init__(self, row_number, cells):

        assert (isinstance(row_number, int))
        assert (isinstance(cells, list))

        self.set_type()
        self.missing_values = []  # list of numbers that have not been found yet
        self.internal_list = []
        self.row_number = row_number

        if isinstance(cells[0], Cell):  # if cells are already converted, don't reconvert, just add
            self.extend(cells)
            self.internal_list = []  # Raw values of cells
            for cell in cells:
                self.internal_list.append(cell.value)
        else:
            for column, value in enumerate(cells):
                cell = Cell(column=column, row=row_number, value=value)
                self.add(cell)
            self.internal_list.append(cell.value)

        self.update_missing_values()

        self.solved = False if self.sum() == 45 else True

    def add(self, cell):
        # make sure cell is a cell
        # make sure cell doesn't already exist in this row,
        # that it's not putting us over our limit (Both should never happen)
        # that it's within the range of acceptable values
        if not isinstance(cell, Cell):
            raise TypeError("Expecting {0}, got {1}".format(Cell, type(cell)))

        elif cell.value in self.internal_list and cell != 0:
            a = cell.value in self.internal_list
            b = cell != 0
            raise ValueError(
                "{0} is already present at position {1}, {2}: {3}".format(cell, self.row_number, self.index(cell),
                                                                          cell.__dict__))

        elif self.sum() + cell > 45:
            raise ValueOutOfBoundsError(cell)

        elif cell.value not in range(0, 9 + 1):
            raise ValueOutOfBoundsError(cell)

        self.append(cell)

    def sum(self):
        return sum(self)

    def update_missing_values(self):
        possible_values = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # this doesn't need to be changed.
        self.missing_values = possible_values - set(self.internal_list)
        return self.missing_values



    def set_cell(self, cell_number, value):
        self[cell_number].set(value)

        # Update possible values in cells
        for cell in self:
            if value in cell.possible_values:
                cell.possible_values.remove(value)

    def set_type(self):
        self.type = "Row"
