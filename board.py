from box import Box
from column import Column
from row import Row


class Board:
    def __init__(self, set_file):
        self.box = []
        self.column = []
        self.row = []
        with open(set_file, 'r') as file:
            content = file.readlines()

            if len(content) != 9:
                raise ValueError("Invalid Set file! File must have 9 lines")

            content = [line.strip() for line in content]
            content = [line.split(',') for line in content]

            for row_number, row_contents in enumerate(content):
                self.row.append(Row(row_number, row_contents))

            # Set Box vales
            for i in range(0, len(self.row)):
                self.box.append(self.generate_boxes(i))

            # set up columns
            self.generate_columns()

    def generate_boxes(self, box_number):
        box = []

        if box_number == 0:
            box.extend(self.row[0][0:3])
            box.extend(self.row[1][0:3])
            box.extend(self.row[2][0:3])

        if box_number == 1:
            box.extend(self.row[0][3:6])
            box.extend(self.row[1][3:6])
            box.extend(self.row[2][3:6])

        if box_number == 2:
            box.extend(self.row[0][6:9])
            box.extend(self.row[1][6:9])
            box.extend(self.row[2][6:9])

        if box_number == 3:
            box.extend(self.row[3][0:3])
            box.extend(self.row[4][0:3])
            box.extend(self.row[5][0:3])

        if box_number == 4:
            box.extend(self.row[3][3:6])
            box.extend(self.row[4][3:6])
            box.extend(self.row[5][3:6])

        if box_number == 5:
            box.extend(self.row[3][6:9])
            box.extend(self.row[4][6:9])
            box.extend(self.row[5][6:9])

        if box_number == 6:
            box.extend(self.row[6][0:3])
            box.extend(self.row[7][0:3])
            box.extend(self.row[8][0:3])

        if box_number == 7:
            box.extend(self.row[6][3:6])
            box.extend(self.row[7][3:6])
            box.extend(self.row[8][3:6])

        if box_number == 8:
            box.extend(self.row[6][6:9])
            box.extend(self.row[7][6:9])
            box.extend(self.row[8][6:9])
        return Box(box_number, box)

    def generate_columns(self):
        for i in range(len(self.row[0])):  # length of first row.
            c = []
            for j in range(len(self.row[0])):
                c.append(self.row[j][i])
            column = Column(row_number=i, cells=c)
            self.column.append(column)
        return

    def get_cell(self, column_coord, row_coord):
        return self.row[row_coord][column_coord]

    def update_possible_values(self, column_coord, row_coord, box_num):
        """
        This must be called from a board in order to supply the values of the box and column
        Column parameter must correspond with the column value of the cell.
        :param column_coord: the column number the cell belongs to.
        :param row_coord: the row number the cell belongs to
        :param box_num: the box number the cell belongs to.
        """
        # TODO: WORK ON THIS. Function not created yet
