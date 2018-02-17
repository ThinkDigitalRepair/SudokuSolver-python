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
            self.update_possible_values()

    def add_box_values(self):
        for box in self.box:
            for cell in box:
                cell.box = box.number

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

        b = Box(box_number, box)

        for cell in b:
            cell.box = box_number

        return b

    def generate_columns(self):
        for i in range(len(self.row[0])):  # length of first row.
            c = []
            for j in range(len(self.row[0])):
                c.append(self.row[j][i])
            column = Column(number=i, cells=c)
            self.column.append(column)
        return

    def get_cell(self, column_coord, row_coord):
        return self.row[row_coord][column_coord]

    @property
    def ordered_by_completeness(self):
        """

        :return: row, column, box with the least unsolved values.
        """
        row_order = {}
        for row in self.row:
            row_order[str(row.number)] = row.unsolved_count

        row_min = min(row_order, key=row_order.get)

        column_order = {}
        for column in self.column:
            column_order[str(column.number)] = column.unsolved_count

        column_min = min(column_order, key=column_order.get)

        box_order = {}
        for box in self.box:
            box_order[str(box.number)] = box.unsolved_count

        box_min = min(box_order, key=box_order.get)
        return {"row_min": row_min, "column_min": column_min, "box_min": box_min}

    def update_possible_values(self):

        """ """
        # TODO: Check to see why so many values are being added to possible_values for each cell

        for row in self.row:
            for cell in row:
                if cell == 0:
                    print("{0} = {1}-{2}-{3}\n {4}\n".format(cell.__dict__, set(self.row[cell.row].missing_values),
                                                             set(self.column[cell.column].found_values),
                                                             set(self.box[cell.box].found_values),
                                                             set(self.row[cell.row].missing_values) - set(
                                                                 self.column[cell.column].found_values) - set(
                                                                 self.box[cell.box].found_values)))
                    cell.possible_values.append(
                        set(self.row[cell.row].missing_values) - set(self.column[cell.column].found_values) - set(
                            self.box[cell.box].found_values))
