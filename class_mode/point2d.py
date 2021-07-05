import numpy as np

class TPoint(object):

    def __init__(self, x = 0, y = 0):
        self.point = np.array([x, y])

    def midpoint(self, other):
        pnt = (self.point + other.point) / 2
        return TPoint(pnt[0], pnt[1])

    def add(self, other):
        pnt = self.point + other.point
        return TPoint(pnt[0], pnt[1])
