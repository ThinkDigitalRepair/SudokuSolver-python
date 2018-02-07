from row import Row


class Board(list):
    def __init__(self, set_file):
        with open(set_file, 'r') as file:
            content = file.readlines()
            if len(content) != 9:
                raise ValueError("Invalid Set file! File must have 9 lines")

            content = [line.strip() for line in content]
            content = [line.split(',') for line in content]

            for row_number, row_contents in enumerate(content):
                self.append(Row(row_number, row_contents))

            # Set Box vales
            self.box = []
            for i in range(0, len(self)):
                a = i
                self.box.append(self.get_box(i))

    def get_box(self, box_number):
        box = []

        if box_number == 0:
            box.extend(self[0][0:3])
            box.extend(self[1][0:3])
            box.extend(self[2][0:3])

        if box_number == 1:
            box.extend(self[0][3:6])
            box.extend(self[1][3:6])
            box.extend(self[2][3:6])

        if box_number == 2:
            box.extend(self[0][6:9])
            box.extend(self[1][6:9])
            box.extend(self[2][6:9])

        if box_number == 3:
            box.extend(self[3][0:3])
            box.extend(self[4][0:3])
            box.extend(self[5][0:3])

        if box_number == 4:
            box.extend(self[3][3:6])
            box.extend(self[4][3:6])
            box.extend(self[5][3:6])

        if box_number == 5:
            box.extend(self[3][6:9])
            box.extend(self[4][6:9])
            box.extend(self[5][6:9])

        if box_number == 6:
            box.extend(self[6][0:3])
            box.extend(self[7][0:3])
            box.extend(self[8][0:3])

        if box_number == 7:
            box.extend(self[6][3:6])
            box.extend(self[7][3:6])
            box.extend(self[8][3:6])

        if box_number == 8:
            box.extend(self[6][6:9])
            box.extend(self[7][6:9])
            box.extend(self[8][6:9])
        return box
