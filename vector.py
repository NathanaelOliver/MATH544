class Vector:
    def __init__(self, v = []):
        self.vector = v

    def __getitem__(self, arg):
        return self.vector[arg]

    def __len__(self):
        return len(self.vector)

    def __str__(self, spacingDist=-1):
        spacingDist = self.get_spacing() if spacingDist == -1 else spacingDist
        cat = "".join([(spacingDist-(len(v.__str__())+1)//2)*" "+v.__str__()+(spacingDist-len(v.__str__())//2+1)*" " for v in self.vector])
        return cat

    def append(self, item):
        self.vector.append(item)

    def __iter__(self):
        for x in self.vector:
            yield x

    def get_spacing(self):
        return max([len(v.__str__())+1 for v in self.vector])//2
    
    def clear(self):
        self.vector = []
