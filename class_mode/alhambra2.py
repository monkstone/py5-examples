from py5 import Sketch
import numpy as np

"""
alhambra.py by Martin Prout
Alhambra tiling in py5
Colors chosen to be a bit nearer the original (also corrected orientation),
and added stars to the non drawn triangles.
Utilizes a custom lightweight TPoint (to replace the more fattening PVector)
"""
from point2d import TPoint
from math import sqrt, sin, cos, pi

GOLD = 0
BLACK = 1
GREEN = 2
BLUE = 3
RED = 4
WHITE = 5
SQRT3 = sqrt(3)

def adjust_bezier(bzpoint, theta, disp):
    """
    Adjust the Bezier control point
    """
    bzpoint.add(TPoint(cos(theta)*disp, sin(theta)*disp))

odd = lambda num: np.arange(1,num*2+1,2)

class Alhambra(Sketch):
    def settings(self):
        self.size(1280, 906)

    def setup(self):
        global colors, x_values, y_values
        x_values = np.multiply(100, odd(8))
        factor = 50 * SQRT3
        y_values = np.multiply(factor, odd(6))
        colors = [
           self.color(151, 84, 5),
           self.color(33, 3, 3),
           self.color(21, 69, 43),
           self.color(27, 51, 121),
           self.color(59, 17, 1),
           self.color(211, 200, 200)
        ]
        self.background(colors[WHITE])
        self.render()

    def draw_star(self, point, sz, col):
        """
        draw star shape function
        """
        self.no_stroke()
        self.fill(col)
        self.triangle(point[0] + sz/SQRT3, point[1], point[0] - (SQRT3*sz)/6, point[1] - 0.5 * sz, point[0] - (SQRT3*sz)/6, point[1] + 0.5 * sz)
        self.triangle(point[0] - sz/SQRT3, point[1], point[0] + (SQRT3*sz)/6, point[1] - 0.5 * sz, point[0] + (SQRT3*sz)/6, point[1] + 0.5 * sz)

    def draw_hexagon(self, point, sz, theta):
        """
        hexagon draw function
        """
        self.fill(colors[WHITE])
        self.begin_shape()
        for i in range(0, 6):
            self.vertex(point[0] + sz*cos((pi/3 * i) + theta), ypos + sz*sin((pi/3 * i) +theta))
        self.end_shape(self.CLOSE)


    def draw_triangle(self, point, sz, coluer, disp):
        """
        Wavy triangle draw function
        """
        # Set the three initial triangle points, thereafter calculate mid points, and
        # quarter points. Then adjust the bezier curve control points.
        pts = []
        pts.append(point.add(TPoint(0, sz/SQRT3)))               # A (A, B and C are the triangle points)
        pts.append(point.add(TPoint(-0.5 * sz, (SQRT3*sz)/6))) # B
        pts.append(point.add(TPoint(0.5 * sz, (SQRT3*sz)/6))) # C
        pts.append(pts[0].midpoint(pts[1]))                        # Ab (Ab, Bc and Ca are the triangle mid points)
        pts.append(pts[1].midpoint(pts[2]))                        # Bc
        pts.append(pts[0].midpoint(pts[2]))                        # Ca
        pts.append(pts[0].midpoint(pts[3]))                        # Aba (Aba ... are the triangle quarter points)
        adjust_bezier(pts[6], -pi/3, -disp*sz)                      # Aba
        pts.append(pts[3].midpoint(pts[1]))                        # Abb
        adjust_bezier(pts[7], -pi/3, disp*sz)                       # Abb
        pts.append(pts[1].midpoint(pts[4]))
        adjust_bezier(pts[8], -pi/2, disp*sz)
        pts.append(pts[4].midpoint(pts[2]))
        adjust_bezier(pts[9], -pi/2, -disp*sz)
        pts.append(pts[2].midpoint(pts[5]))
        adjust_bezier(pts[10], pi/3, disp*sz)
        pts.append(pts[5].midpoint(pts[0]))
        adjust_bezier(pts[11], pi/3, -disp*sz)
        # render triangle
        self.fill(coluer)
        self.begin_shape()
        self.vertex(pts[0][0], pts[0][1])
        self.bezier_vertex(pts[0][0], pts[0][1], pts[6][0], pts[6][1], pts[3][0], pts[3][1])
        self.bezier_vertex(pts[3][0], pts[3][1], pts[7][0], pts[7][1], pts[1][0], pts[1][1])
        self.bezier_vertex(pts[1][0], pts[1][1], pts[8][0], pts[8][1], pts[4][0], pts[4][1])
        self.bezier_vertex(pts[4][0], pts[4][1], pts[9][0], pts[9][1], pts[2][0], pts[2][1])
        self.bezier_vertex(pts[2][0], pts[2][1], pts[10][0], pts[10][1], pts[5][0], pts[5][1])
        self.bezier_vertex(pts[5][0], pts[5][1], pts[11][0], pts[11][1], pts[0][0], pts[0][1])
        self.end_shape(self.CLOSE)
        self.draw_hexagon(TPoint(point[0] - 4, point[1]), sz * 0.22, 0)

    def render(self):
        """
        Tesselate the wavy triangles, add some star in the spaces
        """
        for column in range(8):
            for row in range(6):
                if (row % 2 == 0):
                    self.draw_triangle(TPoint(x_values[column], y_values[row]), 200, colors[(1 + column)%5], 0.32)
                    self.draw_star(TPoint(x_values[column] - 95, y_values[row] + 60), 70, colors[(2 + column)%5])
                else:
                    self.draw_triangle(TPoint(x_values[column] - 100, y_values[row]), 200, colors[column%5], 0.32)
                    self.draw_star(TPoint(x_values[column] + 5, y_values[row] + 60), 70, colors[(2 + column)%5])

alhambra = Alhambra()
alhambra.run_sketch()
