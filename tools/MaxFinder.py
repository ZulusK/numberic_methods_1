class MaxFinder:
    def __init__(self):
        self.max = float("-inf")

    def visit(self, value):
        if value > self.max:
            self.max = value
