from vector import Vector
from multistring import MultiString


class Matrix:
    def identity(row_num, col_num):
        a = Matrix()
        for i in range(0, row_num):
            v = Vector([0]*col_num)
            v[i] = 1
            a.add_row(v)
        return a

    def __init__(self):
        self.matrix = []
        self.row_length = -1
        self.col_length = 0
        self.partition = []

    def get_row(self, arg):
        return self.matrix[arg]

    def get_col(self, col):
        v = Vector()
        v.clear()
        for r in self.matrix:
            v.append(r[col])
        return v

    def add_row(self, row):
        '''
        Adds a row to the matrix

        If the length of the vector being added does not match the row length the method returns false

        @param row the row to be added to the matrix
        @return A boolean indicating whether the row was successfully added or not
        '''
        if self.row_length == -1:
            self.row_length = len(row)
        elif len(row) != self.row_length:
            return False
        self.matrix.append(row)
        self.col_length += 1
        return True

    def add_col(self, col):
        if (len(col) == len(self.matrix)):
            for i in range(len(col)):
                self.matrix[i].add(col[i])

    def add_partition(self, i):
        self.partition.append(i)

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
            if (i+1) in self.partition:
                ret.add([" |"]*self.col_length)
        ret.add(end, " ")
        return ret.__str__()

    def show_step(self, show_steps, instruction):
        if show_steps:
            print(instruction)
            print(self)

    def locate_pivot(self, show_steps,  max_row, r=0, c=0):
        while c < max_row and self.matrix[r][c] == 0:
            for r2 in range(r+1, self.col_length):
                if self.matrix[r2][c] != 0:
                    permutation = self.swap_row(r, r2)
                    self.print_step(show_steps, "Permute rows " +
                                    str(r+1) + " and " + str(r2+1))
                    return permutation, r, c
            else:
                c += 1
        return Matrix.identity(self.col_length, self.row_length), r, c

    def swap_row(self, r1, r2):
        self.matrix[r1], self.matrix[r2] = self.matrix[r2], self.matrix[r1]
        permutation = Matrix.identity(self.col_length, self.row_length)
        permutation[r1], permutation[r2] = permutation[r2], permutation[r1]
        return permutation

    def reduce_row(self, show_steps, row, col):
        pivot = self.matrix[row][col]
        for i in range(len(self.matrix[row])):
            self.matrix[row][i] = self.matrix[row][i] / pivot
        self.show_step(show_steps, "Divide Row " + str(row + 1) + " by " +
                       str(pivot) + " to reduce pivot to 1")

    def subtract_row(self, row, scale, vector):
        for j in range(self.row_length):
            self.matrix[row][j] -= scale*vector[j]

    def rref(self, max_row, show_steps=False):
        row = col = 0
        print(self.col_length)
        print(max_row)
        while row != self.col_length and col != max_row:
            '''Finds the next value in the column and swaps it if there is a zero
            If the rest of the column is 0's, it moves on to the next column'''
            permute, row, col = self.locate_pivot(
                show_steps, max_row, row, col)
            if col == max_row:
                return self
            '''Divides each element in the row by the pivot
            Ensures the pivot is equal to 1'''
            self.reduce_row(show_steps, row, col)
            '''Subtracts each row to make sure that all other elements in the column are 0'''
            for i in range(self.col_length):
                self.subtract_row(
                    i, self.matrix[i][col], self.matrix[row]) if row != i else ""
            row += 1
            col += 1
            self.show_step(show_steps, "Subtracted row " + str(row) +
                           " from other rows to get into row echelon form")
        return self

    def ref(self, max_row, show_steps=False):
        row = col = 0
        print(self.col_length)
        print(max_row)
        while row != self.col_length and col != max_row:
            '''Finds the next value in the column and swaps it if there is a zero
            If the rest of the column is 0's, it moves on to the next column'''
            permute, row, col = self.locate_pivot(
                show_steps, max_row, row, col)
            if col == max_row:
                return self
            '''Divides each element in the row by the pivot
            Ensures the pivot is equal to 1'''
            self.reduce_row(show_steps, row, col)
            '''Subtracts each row to make sure that all other elements in the column are 0'''
            for i in range(row+1, self.col_length):
                self.subtract_row(i, self.matrix[i][col], self.matrix[row])
            row += 1
            col += 1
            self.show_step(show_steps, "Subtracted row " + str(row) +
                           " from other rows to get into row echelon form")
        return self
