

from shapes.encoding import ShapeEncoding
from fitness.composite_fitness import fitness

class Individual:
    def __init__(self, encoding=None):
        self.encoding = encoding or ShapeEncoding()
        self.score = None

    def evaluate(self):
        self.score = fitness(self.encoding)
        return self.score
