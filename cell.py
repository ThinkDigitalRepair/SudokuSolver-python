from color import Color


class PossibleValues(set):
    is_already_set = False

    def __init__(self):
        super().__init__()

    def add(self, value):

        """

        :param value: the value to add to the list
        :return: success if the value is added
        """
        if hasattr(value, '__iter__'):  # If it's a list, then
            for item in value:  # for every item in the list
                    if self.__len__() < 9:
                        super().add(item)
                    else:
                        raise IndexError("This is putting us over 9!")
        elif self.__len__() < 9:
            super().add(value)
        else:
            raise IndexError("This is putting us over 9!")
        return True


class Cell:

    def __init__(self, row, column, value=0, box=0):
        self.row = row
        self.column = column
        self.value = int(value)
        self.box = box
        self.possible_values = PossibleValues()

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
        if self.value == 0:
            return Color.RED + str(self.value) + Color.END
        else:
            return str(self.value)

    def set(self, value):
        self.value = int(value)

    def to_int(self):
        return self.value
