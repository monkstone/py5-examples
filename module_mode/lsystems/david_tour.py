import py5
from math import cos, pi, sin, sqrt, radians
from grammar import grammar
from collections import namedtuple

########################################################
# A David Tour fractal implemented using a
# Lindenmayer System in py5 by Martin Prout
########################################################
w = 600
h = 600

LSystem = namedtuple('DavidTour', 'start, rules, turn_angle_deg')

david = LSystem(
        start = 'FX-XFX-XFX-XFX-XFX-XF',
        rules = dict(
            F = '!F!-F-!F!',
            X = '!X'
            ),
        turn_angle_deg = 60
    )

def settings():
    py5.size(w, h)

def setup():
    sketch_title('David Tour')
    production = grammar.generate(david, 5)
    py5.background(0, 0, 255)
    py5.stroke(255, 255, 0)
    py5.stroke_weight(3)
    render(production)

def render(production):
    """
    Render evaluates the production string and calls draw_line
    """
    delta = radians(david.turn_angle_deg)
    distance = 5
    swap = False
    turtle = {'x': w * 0.65, 'y': h * 0.25, 'angle': 0}
    for val in production:
        if val == 'F':
            turtle = draw_line(turtle, distance)
        elif val == '-':
            turtle['angle'] += delta if swap else -delta
        elif val == '!':
            swap = not swap
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
