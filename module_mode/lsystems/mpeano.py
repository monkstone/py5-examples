
"""
mpeano.py by Martin Prout
LSystem rules from The Euclidean Traveling Salesman Problem.... by MG Norman & P Moscato.
Features a scaling adjustment and turtle reversing, use trignometry rather than processing affine
transforms to calculate the line, uses a grammar module to create production string.
"""
import py5
from math import cos, pi, sin, sqrt
from grammar import grammar

# some globals
XPOS = 0
YPOS = 1
ANGLE = 2
DELTA = py5.PI / 4

RULES = {
'F' : '',
'Y': 'FFY',
'X' : '+!X!FF-BQFI-!X!FF+',
'A' : 'BQFI',
'B' : 'AFF'
}

AXIOM = 'XFF2-AFF2-XFF2-AFF'

def render(production):
    """
    Render evaluates the production string and calls draw_line
    """
    delta = DELTA
    distance = 15
    turtle = [py5.width/10, py5.height/10, -delta]
    repeat = 1
    for val in production:
        if val == "F":
            turtle = draw_line(turtle, distance)
        elif val == "+":
            turtle[ANGLE] += delta * repeat
            repeat = 1
        elif val == "-":
            turtle[ANGLE] -= delta * repeat
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
    turtlecopy = []
    turtlecopy[:] = turtle
    turtlecopy[XPOS] = turtle[XPOS] + length * cos(turtle[ANGLE])
    turtlecopy[YPOS] = turtle[YPOS] - length * sin(turtle[ANGLE])
    py5.line(turtle[XPOS], turtle[YPOS], turtlecopy[XPOS], turtlecopy[YPOS])
    return turtlecopy

def settings():
    py5.size(600, 600)

def setup():
    sketch_title('MPeano')

    production = grammar.repeat(6, AXIOM, RULES)
    py5.background(0, 0, 255)
    py5.stroke(255, 255, 0)
    py5.stroke_weight(3)
    render(production)

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
