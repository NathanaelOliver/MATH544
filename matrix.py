class Matrix:
    def __init__(self, matrix = []):
        self.matrix = matrix

    def get_row(self, arg):
        return self.matrix[arg]

    def get_col(self, col):
        v = Vector()
        for r in self.matrix:
            v.append(r[col])

    def add_row(self, row):
        self.matrix.append(row)

    def add_col(self, col):
        if (len(col) == len(self.matrix)):
            for i in range(len(col)):
                self.matrix[i].add(col[i])

    def __str__(self):
        spacing = max([row.get_spacing() for row in self.matrix])
        cat = "⸢ " + self.matrix[0].__str__(spacing) +"⸣\n"
        cat += "".join(["| "+self.matrix[v].__str__(spacing) +"|\n" for v in range(1,len(self.matrix)-1)])
        return cat +"⸤ " + self.matrix[-1].__str__(spacing) + "⸥"

class Vector:
    def __init__(self, v = []):
        self.vector = v

    def __getitem__(self, arg):
        return self.vector[arg]

    def __len__(self):
        return len(self.v)

    def __str__(self, spacingDist=-1):
        spacingDist = self.get_spacing() if spacingDist == -1 else spacingDist
        cat = "".join([(spacingDist-(len(v.__str__())+1)//2)*" "+v.__str__()+(spacingDist-len(v.__str__())//2+1)*" " for v in self.vector])
        return cat

    def get_spacing(self):
        return max([len(v.__str__())+1 for v in self.vector])//2 


