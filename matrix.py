from vector import Vector
from multistring import MultiString

class Matrix:
    def __init__(self, matrix = []):
        self.matrix = matrix

    def get_row(self, arg):
        return self.matrix[arg]

    def get_col(self, col):
        v = Vector()
        v.clear()
        for r in self.matrix:
            v.append(r[col])
        return v

    def add_row(self, row):
        self.matrix.append(row)

    def add_col(self, col):
        if (len(col) == len(self.matrix)):
            for i in range(len(col)):
                self.matrix[i].add(col[i])

    def __str__(self):
        if len(self.matrix) == 0:
            return "[]"
        start = ["⸢"]
        start.extend((["|"]*(len(self.matrix)-2)))
        start.append("⸤")
        end = ["⸣"]
        end.extend((["|"]*(len(self.matrix)-2)))
        end.append("⸥")
        ret = MultiString(start)
        for i in range(len(self.matrix[0])):
            ret.add(self.get_col(i), " ")
        ret.add(end, " ")
        return ret.__str__()

    def rref(self, show_steps = False):
        pass