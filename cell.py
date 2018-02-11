class PossibleValues(list):
    def update(self, value):
        """

        :param value: the value to add to the list
        :return: success if the value is added
        """
        if self.__len__() >= 9:
            raise IndexError
        else:
            self.update(value)
        return True


class Cell:
    possible_values = PossibleValues()

    def __init__(self, row, column, value=0):
        self.row = row
        self.column = column
        self.value = int(value)

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
        return str(self.value)

    def set(self, value):
        self.value = int(value)
        return
