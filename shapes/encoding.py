import numpy as np

"""
Represents a parametric architectural form. 
E.g. control points for Bezier curves, radii for circles, etc.
"""
class ShapeEncoding:
    def __init__(self, control_points=None):
        if control_points is None:
            control_points = np.random.rand(5, 2)  # 5 random points
        self.control_points = control_points

    def mutate(self, rate=0.1):
        noise = np.random.randn(*self.control_points.shape) * rate
        self.control_points += noise

    def crossover(self, other):
        cp = (self.control_points + other.control_points) / 2
        return ShapeEncoding(cp)