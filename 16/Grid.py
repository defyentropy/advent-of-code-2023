class Grid:
    def __init__(self, grid_data):
        self.rows = []
        self.NUM_ROWS = len(grid_data)
        self.NUM_COLS = len(grid_data[0])

        for grid_row in grid_data:
            row = []
            for el in grid_row:
                row.append(el)
            self.rows.append(row)

    def at(self, pos):
        try:
            return self.rows[pos[1]][pos[0]]
        except IndexError:
            return None

    def set_at(self, pos, new):
        self.rows[pos[1]][pos[0]] = new

    def get_row(self, index):
        return self.rows[index].copy()

    def get_col(self, index):
        col = []
        for row in self.rows:
            col.append(row[index])
        return col

    def insert_row(self, index, row):
        self.rows.insert(index, row.copy())
        self.NUM_ROWS += 1

    def insert_col(self, index, column):
        for i, el in enumerate(column):
            self.rows[i].insert(index, el)
        self.NUM_COLS += 1

    @staticmethod
    def manhattan_distance(pos1, pos2):
        return abs(pos2[1] - pos1[1]) + abs(pos2[0] - pos1[0])

    def find(self, target):
        matches = []

        for i, row in enumerate(self.rows):
            for j, el in enumerate(row):
                if el == target:
                    matches.append((j, i))

        return matches

    def __repr__(self):
        return "\n".join(["".join(row) for row in self.rows])
