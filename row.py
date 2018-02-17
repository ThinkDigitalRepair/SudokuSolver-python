from cell import Cell
from error import *


class Row(list):

    def __init__(self, number, cells):

        assert (isinstance(number, int))
        assert (isinstance(cells, list))

        self.set_type()
        self.number = number

        if isinstance(cells[0], Cell):  # if cells are already converted, don't reconvert, just add
            self.extend(cells)
        else:
            for column, value in enumerate(cells):
                cell = Cell(column=column, row=number, value=value)
                self.add(cell)

    @property
    def internal_list(self):
        # TODO: Update this later to not run if no changes are made to optimize processing
        internal_list = []  # Raw values of cells
        for cell in self:
            internal_list.append(cell.value)
        return internal_list

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
                "{0} is already present at position {1}, {2}: {3}".format(cell, self.number,
                                                                          self.internal_list.index(cell.value),
                                                                          cell.__dict__))

        elif self.sum() + cell > 45:
            raise ValueOutOfBoundsError(cell)

        elif cell.value not in range(0, 9 + 1):
            raise ValueOutOfBoundsError(cell)

        self.append(cell)

    def sum(self):
        return sum(self)

    @property
    def missing_values(self):
        return {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(self.internal_list)

    def set_cell(self, cell_number, value):
        self[cell_number].set(value)

        # Update possible values in cells
        for cell in self:
            if value in cell.possible_values:
                cell.possible_values.remove(value)

    def set_type(self):
        self.type = "Row"

    @property
    def solved(self):
        return False if self.sum() == 45 else True

    @property
    def found_values(self):
        found_values = set(self.internal_list)
        found_values.remove(0)
        return found_values

    @property
    def unsolved_count(self):
        """
        :return: cells that are unsolved (whose value is still 0
        """
        return self.count(0)
