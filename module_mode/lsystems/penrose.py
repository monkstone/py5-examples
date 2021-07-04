"""
penrose.py processing sketch by Martin Prout, but uses LSystem rules from a Fractint sketch
by Herb Savage which in turn is based on Martin Gardner's "Penrose Tiles to Trapdoor Ciphers",
Roger Penrose's rhombuses.
This sketch uses a grammar module as before, here the output is a pdf file. Wait until
the penrose appears before closing the applet (NB the text does not appear in the applet,
but should be in the pdf file). You will probably need to edit the path to ttf fonts to
match your system (apparently pdf export doesn't work well for non ttf fonts).
"""
import py5
from math import cos, sin
from grammar import grammar

# some globals
XPOS = 0
YPOS = 1
ANGLE = 2
DELTA = py5.TWO_PI / 10

RULES = {
    'F' : '',
    'W' : 'YBF2+ZRF4-XBF[-YBF4-WRF]2+',
    'X' : '+YBF2-ZRF[3-WRF2-XBF]+',
    'Y' : '-WRF2+XBF[3+YBF2+ZRF]-',
    'Z' : '2-YBF4+WRF[+ZRF4+XBF]2-XBF'
}

AXIOM = '[X]2+[X]2+[X]2+[X]2+[X]'


def render(production):
    """
    Render evaluates the production string and calls draw_line
    """
    turtle = [0, 0, -DELTA]
    stack = []
    repeat = 1
    for val in production:
        if val == 'F':
            turtle = __draw_line(turtle, 20)
        elif val == '+':
            turtle[ANGLE] += DELTA * repeat
            repeat = 1
        elif val == '-':
            turtle[ANGLE] -= DELTA * repeat
            repeat = 1
        elif val == '[':      # an unfortunate aggregation of square brackets
            temp = []
            temp[:] = turtle
            stack.append(temp)
        elif val == ']':
            turtle = stack.pop()
        elif ((val == '2') or (val == '3') or (val == '4')):
            repeat = int(val)
        else:
            pass


def __draw_line(turtle, length):
    """
    private line draw uses processing 'line' function to draw a line
    to a heading from the turtle with distance = length returns a new
    turtle corresponding to end of the new line
    """
    turtlecopy = []
    turtlecopy[:] = turtle
    turtlecopy[XPOS] = turtle[XPOS] + length * cos(turtle[ANGLE])
    turtlecopy[YPOS] = turtle[YPOS] - length * sin(turtle[ANGLE])
    py5.line(turtle[XPOS], turtle[YPOS], turtlecopy[XPOS], turtlecopy[YPOS])
    return turtlecopy

def add_text():
    my_font = py5.create_font('FreeSans', 18)
    py5.fill(0, 0, 200)
    py5.text_font(my_font, 18)
    py5.text("Penrose Tiling", 300, 50)
    py5.text(grammar.rule_text(AXIOM, RULES), 100, 650)

def settings():
    py5.size(700, 900)

def setup():
    sketch_title('LSystems Penrose')
    py5.background(255)
    production = grammar.repeat(5, AXIOM, RULES)
    add_text()
    py5.stroke_weight(2)
    py5.translate(py5.width / 2, py5.height * 0.4)
    render(production)

def sketch_title(title):
    py5.get_surface().set_title(title)


py5.run_sketch()
