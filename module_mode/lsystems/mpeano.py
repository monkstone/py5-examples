import py5
from math import cos, pi, sin, sqrt, radians
from grammar import grammar
from collections import namedtuple

"""
mpeano.py by Martin Prout
LSystem rules from The Euclidean Traveling Salesman Problem.... by MG Norman & P Moscato.
Features a scaling adjustment and turtle reversing, use trignometry rather than processing affine
transforms to calculate the line, uses a grammar module to create production string.
"""

w = 600
h = 600

LSystem = namedtuple('MPeano', 'start, rules, turn_angle_deg')

mpeano = LSystem(
        start = 'XFF2-AFF2-XFF2-AFF',
        rules = dict(
            F = '',
            Y = 'FFY',
            X = '+!X!FF-BQFI-!X!FF+',
            A = 'BQFI',
            B = 'AFF'
            ),
        turn_angle_deg = 45
    )

def settings():
    py5.size(w, h)

def setup():
    sketch_title('MPeano')

    production = grammar.generate(mpeano, 6)
    py5.background(0, 0, 255)
    py5.stroke(255, 255, 0)
    py5.stroke_weight(3)
    render(production)

def render(production):
    """
    Render evaluates the production string and calls draw_line
    """
    delta = radians(mpeano.turn_angle_deg)
    distance = 15
    turtle = {'x': w / 10, 'y': h / 10, 'angle': -delta}
    repeat = 1
    for val in production:
        if val == "F":
            turtle = draw_line(turtle, distance)
        elif val == "+":
            turtle['angle'] += delta * repeat
            repeat = 1
        elif val == "-":
            turtle['angle']-= delta * repeat
            repeat = 1
        elif val == "I":
          distance *= 1/sqrt(2)
        elif val == "Q":
            distance *= sqrt(2)
        elif val == "!":
            delta = -delta
        elif (val == '2'):
            repeat = 2
        else:
            pass

def draw_line(turtle, length):
    """
    Draw line utility uses processing 'line' function to draw lines
    """
    turtlecopy = turtle.copy()
    turtlecopy['x'] = turtle['x'] + length * cos(turtle['angle'])
    turtlecopy['y'] = turtle['y'] - length * sin(turtle['angle'])
    py5.line(turtle['x'], turtle['y'], turtlecopy['x'], turtlecopy['y'])
    return turtlecopy

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
