import logging

from color import Color


class Cell:
    logging.getLogger().setLevel(logging.INFO)

    def __init__(self, row, column, value=0, box=0, fixed=False, set_by_function=""):
        """

        :param set_by_function: Optional. The function that determined the cell's value. Mainly used for diagnosis.
        :param row: the row the cell is a part of
        :param column: the column the cell is part of
        :param value: the value of the cell
        :param box: the box the cell is part of
        :param fixed: whether or not this is a fixed cell.
        """
        self.set_by_function = set_by_function
        self.row = row
        self.column = column
        self.value = int(value)
        self.box = box
        self.possible_values = {}
        self.fixed = fixed
        self.colorized = None

    def __eq__(self, other):
        if isinstance(other, int):
            # print("eq == {0}".format(self.value == Cell(0, 0, other).value))
            return self.value == Cell(0, 0, other).value
        else:
            return True

    def __ne__(self, other):
        # print("__ne__: {0}".format(self.value != other))
        return self.value != other

    def __radd__(self, other):
        return self.value + other

    def __repr__(self):
        if self.colorized:  # Colorized options go here
            if self.value == 0:
                return Color.RED + str(self.value) + Color.END
            else:  # these are all values set by the program
                return Color.BLUE + str(self.value) + Color.END
        elif self.fixed or not self.colorized:
            return str(self.value)

    def set(self, value, set_by_function):
        """

        :param value: the value to set
        :param set_by_function: Optional: The function that determined the cell's value.
         Mainly used for diagnosis.

         WARNING: ONLY USE THIS WITH Row().set_cell() because of checks needing to be run!
        """
        if not self.fixed:
            if self.value != 0:
                logging.warning(
                    "{4}\nCell was already set to {0} by {1}. \nValue is now being set to {2} by {3}".format(self.value,
                                                                                                             self.set_by_function,
                                                                                                             value,
                                                                                                             set_by_function,
                                                                                                             self.__dict__))
                raise ValueError(
                    "{4}\nCell was already set to {0} by {1}. \nValue is now being set to {2} by {3}".format(self.value,
                                                                                                             self.set_by_function,
                                                                                                             value,
                                                                                                             set_by_function,
                                                                                                             self.__dict__))
            else:
                self.value = int(value)
                self.set_by_function = set_by_function
                self.possible_values.clear()
        else:
            logging.CRITICAL("Attempting to set a fixed cell!")
            raise ValueError("Attempting to set a fixed cell!")

    def to_int(self):
        return self.value
