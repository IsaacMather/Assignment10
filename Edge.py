class Edge():

    def __init__(self, src, dest, cost = None):
        self.src = src
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost