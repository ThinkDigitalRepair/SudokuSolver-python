import logging
from functools import reduce

from box import Box
from column import Column
from row import Row


class Board:

    def __init__(self, set_file):
        logging.getLogger().setLevel(logging.INFO)

        self.box = []
        self.column = []
        self.row = []
        self.url = ""

        with open(set_file, 'r') as file:
            content = file.readlines()
            content = [line.strip() for line in content]
            content = [line.split(',') for line in content]

            if content[0][0].startswith("http"):
                self.url = content.pop(0)[0]

            for row_number, row_contents in enumerate(content):
                self.row.append(Row(row_number, row_contents))

            # Set Box vales
            for i in range(0, len(self.row)):
                self.box.append(self.generate_boxes(i))

            # set up columns
            self.generate_columns()

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

    def naked_subset(self):
        # TODO: Create Function
        pass

    @property
    def ordered_by_completeness(self):
        """

        :return: row, column, box with the least unsolved values.
        """
        row_order = {}
        for row in self.row:
            if row.unsolved_count != 0:
                row_order[str(row.number)] = row.unsolved_count

        row_min = min(row_order, key=row_order.get)

        column_order = {}
        for column in self.column:
            if column.unsolved_count != 0:
                column_order[str(column.number)] = column.unsolved_count

        column_min = min(column_order, key=column_order.get)

        box_order = {}
        for box in self.box:
            if box.unsolved_count != 0:
                box_order[str(box.number)] = box.unsolved_count

        box_min = min(box_order, key=box_order.get)
        return {"row_min": row_min, "column_min": column_min, "box_min": box_min}

    @property
    def percent_complete(self):
        result = reduce((lambda x, y: x + y), [row.percent_complete for row in self.row]) / 9
        return round(result, 2) * 100

    def set_sole_candidates(self):
        set_cells = []
        for row in self.row:
            for cell in row:
                if len(cell.possible_values) == 1:
                    cell.set(cell.possible_values.pop())
                    set_cells.append(cell)
                    logging.info(msg=cell.__dict__)
        return set_cells

    def solve(self):
        result = ["filler", "text"]

        while len(result) > 0:
            self.update_possible_values()
            result = self.set_sole_candidates()
            pass

    def update_possible_values(self):
        """
        The basic solving of the entire board. This updates the possible values list for each cell.
        """
        updated_cells = []
        for row in self.row:
            for cell in row:
                if cell == 0:
                    cell.possible_values = (
                        set(self.row[cell.row].missing_values) - set(self.column[cell.column].found_values) - set(
                            self.box[cell.box].found_values))

    def __print__(self, colorized=True):
        for row in self.row:
            print(row)
# TODO: scrape http://www.dailysudoku.com/
