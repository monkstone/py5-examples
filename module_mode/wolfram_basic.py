### A basic implementation of rule WM148 in Python mode ###
### doc --> https://www.wolframphysics.org/universes/wm148/ ###
### explanation --> https://www.wolframphysics.org/technical-introduction/basic-form-of-models/first-example-of-a-rule/index.html ###

import py5
VerletPhysics2D = py5.JClass('toxi.physics2d.VerletPhysics2D')
VerletParticle2D = py5.JClass('toxi.physics2d.VerletParticle2D')
VerletSpring2D = py5.JClass('toxi.physics2d.VerletSpring2D')
AttractionBehavior2D = py5.JClass('toxi.physics2d.behaviors.AttractionBehavior2D')
Vec2D = py5.JClass('toxi.geom.Vec2D')
#from py5 import Sketch
from collections import defaultdict
import numpy as np

W, H = 1000, 600 #dimensions of canvas

def settings():
    py5.size(W, H)

def setup():
    global physics, a, sw
    x, y, z = 0, 1, 2
    a = np.array([x, y]) #starting axiom
    sw = []
    # Instantiate Verlet Physics + set drag
    physics = VerletPhysics2D()
    physics.setDrag(.2)

    # RULE: [(x, y)] --> [(x, y), (y, z)]
    for step in range(11):
        temp = [(y, z+i+len(a)-1) for i, (x,y) in enumerate(a)]
        a = sum(zip(a, temp),())

        d = defaultdict(set)
    for n1, n2 in a:
        d[n1].add(n2)
        d[n2].add(n1)

        neighbors_count = sorted(len(d[k]) for k in d)
        minl, maxl = neighbors_count[0], neighbors_count[-1]

        # Get id of each node
        uniques = set(sum(a, ())) # [0, 1, 2, ..., n]

    # Add particle for each node
    for id in uniques:
        p = VerletParticle2D(Vec2D.randomVector().scale(W).add(Vec2D(W>>1, H>>1)))
        physics.addParticle(p)
        physics.addBehavior(AttractionBehavior2D(p, 40, -.5))

    # Create spring between each pair of nodes
    for n1, n2 in a:
        p1 = physics.particles.get(n1)
        p2 = physics.particles.get(n2)
        l = (len(d[n1]) + len(d[n2])) * .5
        f = py5.remap(l, minl, maxl, 1, 0.1)
        s = VerletSpring2D(p1, p2, l*l*f, .3)
        physics.addSpring(s)

        w = l*l*.015
        sw.append(w)



def draw():
    py5.background(255)

    physics.update() #update physics

    #Draw springs + nodes
    for i, s in enumerate(physics.springs):
        py5.stroke_weight(sw[i])
        py5.line(s.a.x(), s.a.y(), s.b.x(), s.b.y())

    py5.push_style()
    py5.stroke_weight(2)
    for p in physics.particles:
        py5.point(p.x(), p.y())
    py5.pop_style()

py5.run_sketch()
