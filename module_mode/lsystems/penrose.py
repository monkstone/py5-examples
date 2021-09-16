import py5
from math import cos, pi, sin, sqrt, radians
from grammar import grammar
from collections import namedtuple

"""
penrose.py processing sketch by Martin Prout, but uses LSystem rules from a Fractint sketch
by Herb Savage which in turn is based on Martin Gardner's `Penrose Tiles to Trapdoor Ciphers`,
Roger Penrose's rhombuses.
This sketch uses a grammar module as before, here the output is a pdf file. Wait until
the penrose appears before closing the applet (NB the text does not appear in the applet,
but should be in the pdf file). You will probably need to edit the path to ttf fonts to
match your system (apparently pdf export doesn't work well for non ttf fonts).
"""

w = 750
h = 900

LSystem = namedtuple('Penrose', 'start, rules, turn_angle_deg')

penrose = LSystem(
        start = '[X]2+[X]2+[X]2+[X]2+[X]',
        rules = dict(
            F = '',
            W = 'YBF2+ZRF4-XBF[-YBF4-WRF]2+',
            X = '+YBF2-ZRF[3-WRF2-XBF]+',
            Y = '-WRF2+XBF[3+YBF2+ZRF]-',
            Z = '2-YBF4+WRF[+ZRF4+XBF]2-XBF'
            ),
        turn_angle_deg = 36
    )

def render(production):
    """
    Render evaluates the production string and calls draw_line
    """
    delta = radians(penrose.turn_angle_deg)
    turtle = {'x': 0, 'y': 0, 'angle': -delta}
    stack = []
    repeat = 1
    for val in production:
        if val == 'F':
            turtle = __draw_line(turtle, 20)
        elif val == '+':
            turtle['angle'] += delta * repeat
            repeat = 1
        elif val == '-':
            turtle['angle'] -= delta * repeat
            repeat = 1
        elif val == '[':      # an unfortunate aggregation of square brackets
            temp = []
            temp = turtle.copy()
            stack.append(temp)
        elif val == ']':
            turtle = stack.pop()
        elif ((val == '2') or (val == '3') or (val == '4')):
            repeat = int(val)
        else:
            pass


def __draw_line(turtle, length):
    """
    Draw line utility uses processing 'line' function to draw lines
    """
    turtlecopy = turtle.copy()
    turtlecopy['x'] = turtle['x'] + length * cos(turtle['angle'])
    turtlecopy['y'] = turtle['y'] - length * sin(turtle['angle'])
    py5.line(turtle['x'], turtle['y'], turtlecopy['x'], turtlecopy['y'])
    return turtlecopy

def add_text():
    my_font = py5.create_font('FreeSans', 18)
    py5.fill(0, 0, 200)
    py5.text_font(my_font, 18)
    py5.text("Penrose Tiling", 300, 50)
    output = str(penrose)
    result  = output.replace(',','\n')
    py5.text(result, 100, 650)

def settings():
    py5.size(w, h)

def setup():
    sketch_title('LSystems Penrose')
    py5.background(255)
    production = grammar.generate(penrose, 5)
    add_text()
    py5.stroke_weight(2)
    py5.translate(w / 2, h * 0.4)
    render(production)

def sketch_title(title):
    py5.get_surface().set_title(title)


py5.run_sketch()
