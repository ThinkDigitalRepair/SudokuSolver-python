import logging

from cell import Cell
from error import *


class Row(list):

    def __init__(self, number, cells):
        super().__init__()
        assert (isinstance(number, int))
        assert (isinstance(cells, list))

        self.set_type()
        self.number = number

        if isinstance(cells[0], Cell):  # if cells are already converted, don't reconvert, just add
            # when initializing Rows, all cells should be fixed, since we won't be initializing Rows
            # during the solving stage
            for cell in cells:
                cell.fixed = True if cell.value != 0 else False

            self.extend(cells)
        else:
            for column, value in enumerate(cells):
                cell = Cell(column=column, row=number, value=value, fixed=True if value != 0 else False)
                self.add(cell)

    @property
    def internal_list(self):
        # TODO: Update this later to not run if no changes are made to optimize processing
        return [cell.value for cell in self]

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

    def __print__(self, colorized=False):
        if colorized:
            for cell in self:
                cell.colorized = True
        print(self)

    def sum(self):
        return sum(self)

    @property
    def missing_values(self):
        return {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(self.internal_list)

    @property
    def percent_complete(self):
        count_ = (9 - self.unsolved_count) / 9
        return round(count_, 2)

    def set_cell(self, cell_number, value, set_by_function: str, remove_from_pv_list=True):
        """
        :param value:
        :param cell_number:
        :param set_by_function: The function that determined the cell's value.
        Mainly used for diagnosis.
        """
        if value not in self.internal_list:
            self[cell_number].set(value, set_by_function=set_by_function)
        else:
            existing_cell = self[self.internal_list.index(value)]
            logging.warning("{0} already exists in this {1}!".format(value, self.type))
            # raise ValueError("{0} already exists in this {1}!".format(value, self.type))

        if remove_from_pv_list:
            # Update possible values in cells
            self.remove_from_pv_lists(value)

    def remove_from_pv_lists(self, value):
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

    def set_hidden_singles(self):
        """
        Find a cell that has a value in it's possible values set that isn't present in any other cell in it's row
        and then remove it from any other cells's possible values list in it's row/column/box
        :return:
        """

        this_rows_possible_values = [cell.possible_values for cell in self]

        pv_list_temp = []
        for pv_list in this_rows_possible_values:  # add all the possible values lists together to search them
            pv_list_temp.extend(pv_list)

        # Find values that only only 1 occurrence.
        hidden_singles = [x for x in pv_list_temp if pv_list_temp.count(x) == 1]

        # Find the cell that has that value in its possible_values list.
        result = []
        if hidden_singles:
            for possible_values_list in this_rows_possible_values:  # Go through each possible_values list in the row and
                for list_index, pv_list in enumerate(this_rows_possible_values):
                    for value in hidden_singles:  # For every hidden single that needs to be set
                        if value in pv_list:  # If it's in this current possible_values list
                            self.set_cell(list_index, value, "Row.set_hidden_singles()",
                                          remove_from_pv_list=True)  # Set the value of the cell to that value.
                            result.append(self[list_index])
                            hidden_singles.remove(value)
        # Return it if its present
        return result

    def naked_pairs(self):
        """
        A Naked Pair (also known as a Conjugate Pair) is a set of two candidate numbers sited in two cells
        that belong to at least one unit in common. That is, they reside in the same row, column or box.

        :return:
        """
        return

    @property
    def unsolved_count(self):
        """
        :return: cells that are unsolved (whose value is still 0
        """
        return self.count(0)
