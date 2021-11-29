
class MultiString:
    # Constructor for the multistring
    def __init__(self, lines = [""]):
        self.lines = MultiString.align_center(lines)

    # Centers an item within its own column
    @staticmethod
    def align_center(lines):
        offset = max([len(line.__str__()) for line in lines])
        return [(offset - len(line.__str__()))//2*" " + line.__str__() + (offset - len(line.__str__())+1)//2*" " for line in lines]


    # Adds an extra column to the multistring
    def add(self, lines, delimeter=""):
        # Ensure the two columns are the same length and centered before adding
        self.lines = MultiString.align_vert(self.lines, max([len(self.lines), len(lines)]))
        lines = MultiString.align_vert(MultiString.align_center(lines), max([len(self.lines), len(lines)]))
        # Add the columns together

        self.lines = [self.lines[i].__str__() +delimeter+ lines[i].__str__() for i in range(0, len(self.lines))]
        
    # Centers column vertically within multistring
    @staticmethod
    def align_vert(lines, length):
        [lines.insert(0, len(lines[0].__str__())*" ") for i in range((length-len(lines))//2)]
        [lines.append(len(lines[0].__str__())*" ") for i in range((length + 1-len(lines))//2)]
        return lines

    # Creates a string representation of the multistring
    def __str__(self):
        return "\n".join(self.lines)