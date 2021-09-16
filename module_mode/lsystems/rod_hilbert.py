'''
Copyright (c) 2021 Martin Prout

This demo is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

hilbert.py by Martin Prout based on a Hilbert curve from 'Algorithmic Beauty
of Plants' by Przemyslaw Prusinkiewicz & Aristid Lindenmayer
and a python lsystem module to provide grammar module.
Features processing affine transforms.
'''
import py5
from collections import namedtuple
from math import pi, sin, cos, radians
from grammar import grammar

ArcBall = py5.JClass('arcball.ArcBall')

# some lsystem constants
XPOS = 0
YPOS = 1
ANGLE = 2
BEN = pi/360   # just a bit of fun set BEN to zero for a regular Hilbert
theta = pi/2   # + BEN
phi = pi/2     # - BEN
distance = 320
depth = 3
# (py5.sq(depth) - 1)/2
adjustment = [0,  0.5,  1.5,  3.5,  7.5]

LSystem = namedtuple('Hilbert', 'start, rules, turn_angle_deg')

hilbert = LSystem(
        start = 'A',
        rules = dict(
            F = '',
            A = 'B>F<CFC<F>D+F-D>F<1+CFC<F<B1^',
            B = 'A+F-CFB-F-D1->F>D-1>F-B1>FC-F-A1^',
            C = '1>D-1>F-B>F<C-F-A1+FA+F-C<F<B-F-D1^',
            D = '1>CFB>F<B1>FA+F-A1+FB>F<B1>FC1^'
            ),
        turn_angle_deg = 90
    )

production = None   # need exposure at module level

def render(production):
    '''
    Render evaluates the production string and calls sphere() and draw_rod()
    uses processing affine transforms (translate/rotate)
    '''
    theta = radians(hilbert.turn_angle_deg)
    phi = radians(hilbert.turn_angle_deg)
    # py5.sphere(distance/7)  # first sphere end cap
    repeat = 1
    for val in production:
        if val == 'F':
            draw_rod(distance)
        elif val == '+':
            py5.rotate_x(theta * repeat)
            repeat = 1
        elif val == '-':
            py5.rotate_x(-theta * repeat)
            repeat = 1
        elif val == '>':
            py5.rotate_y(theta * repeat)
            repeat = 1
        elif val == '<':
            py5.rotate_y(-theta * repeat)
        elif val == '^':
            py5.rotate_z(phi * repeat)
            repeat = 1
        elif (val == '1') :
            repeat = 2
        elif (val == 'A' or val == 'B' or val == 'C' or val == 'D'):
            pass  # assert as valid grammar and do nothing
        else:
            print('Unknown grammar %d'%val)


def draw_rod(distance):
    '''
    Draw a cylinder with length distance, and a sphere at the end
    '''
    sides = 10
    radius = distance / 7
    angle = 0
    angle_increment = pi * 2 / sides
    py5.translate(0, 0, -distance / 2.0)
    py5.begin_shape(py5.QUAD_STRIP)
    for i in range(sides+1):
        py5.normal(cos(angle), sin(angle), 0)
        py5.vertex(radius*cos(angle), radius*sin(angle), -distance/2)
        py5.vertex(radius*cos(angle), radius*sin(angle), distance/2,)
        angle += angle_increment
    py5.end_shape()
    py5.translate(0, 0, -distance/2)
    py5.sphere(radius)

def define_lights():
    py5.fill(191, 191, 191)
    py5.lights()
    py5.directional_light(100, 100, 100, -1, -1, 1)

def evaluate_rules():
    global production,  distance
    production = grammar.generate(hilbert, depth)
    if (depth > 0) :
        distance *= 1/(py5.sq(depth) - 1)

def settings():
    py5.size(500, 500, py5.P3D)

def setup():
    sketch_title('Rod Hilbert')
    evaluate_rules()
    ArcBall(py5.get_current_sketch())
    py5.no_stroke()

def draw():
    '''
    Render a 3D Hilbert/Rod Hilbert, somewhat centered
    '''
    py5.background(10, 10, 200)
    define_lights()
    py5.sphere_detail(11)
    py5.push_matrix()
    py5.translate( distance * adjustment[depth], -distance * adjustment[depth], distance * adjustment[depth])
    render(production)
    py5.pop_matrix()

def key_pressed():
    '''
    User interaction for processing.py
    '''
    global depth, distance
    if (py5.key == '+') and (depth  < 4):
        depth += 1
        distance = 280
        evaluate_rules()
    if (py5.key == '-') and (depth > 1):
        depth -= 1
        distance = 280
        evaluate_rules()

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
