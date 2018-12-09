class MinFinder:
    def __init__(self):
        self.min = float("+inf")

    def visit(self, value):
        if value < self.min:
            self.min = value
