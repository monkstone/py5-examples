### How rule WM686 can be used as a circle growth algorithm ###
### doc --> https://www.wolframphysics.org/universes/wm686/ ###

import py5

VerletPhysics2D = py5.JClass('toxi.physics2d.VerletPhysics2D')
VerletParticle2D = py5.JClass('toxi.physics2d.VerletParticle2D')
VerletSpring2D = py5.JClass('toxi.physics2d.VerletSpring2D')
AttractionBehavior2D = py5.JClass('toxi.physics2d.behaviors.AttractionBehavior2D')
Vec2D = py5.JClass('toxi.geom.Vec2D')
#from py5 import Sketch
from collections import defaultdict
W, H = 1000, 600 #dimensions of canvas


def settings():
    py5.size(W, H)

def setup():
    global physics, a, z
    a = [(0, 1), (0, 2), (1, 2)] #starting axiom
    z = max(sum(a,()))+1 #total number of edges AND the id of the next node to add
    # Instantiate Verlet Physics + set drag
    physics = VerletPhysics2D()
    physics.setDrag(.2)

    # Get id of each node
    uniques = set(sum(a, ())) # [0, 1, 2]

    # Add particle for each node
    for id in uniques:
        p = VerletParticle2D(Vec2D.randomVector().add(Vec2D(W>>1, H>>1)))
        physics.addParticle(p)
        physics.addBehavior(AttractionBehavior2D(p, 10, -.5))

    # Create spring between each pair of nodes
    for n1, n2 in a:
        p1 = physics.particles.get(n1)
        p2 = physics.particles.get(n2)
        s = VerletSpring2D(p1, p2, 4, .5)
        physics.addSpring(s)


def draw():
    py5.background(255)

    global z

    physics.update() #update physics

    # Process rule: [(x, y)] --> [(y, z), (z, x)]
    id = py5.random_int(z - 1)#pick an edge at random
    x, y = a[id] #coordinates of selected edge
    del a[id] #remove edge
    a.extend([(y, z), (z, x)]) #add 2 new edges according to replacement rule

    # Manage physics accordingly
    px = physics.particles.get(x) #coordinate of node x
    py = physics.particles.get(y) #coordinate of node y
    pz = VerletParticle2D(px.add(py).scale(.5)) #create a new particle in between

    s = physics.getSpring(px, py) #find spring between the deleted edge
    physics.removeSpring(s) #remove that spring

    physics.addParticle(pz) #add particle
    physics.addBehavior(AttractionBehavior2D(pz, 10, -.5)) #attach a repulsion behavior to it

    s1 = VerletSpring2D(py, pz, 4, .5) #create spring between 1st new edge
    s2 = VerletSpring2D(pz, px, 4, .5) #create spring between 2nd new edge
    physics.addSpring(s1) #add them to physics
    physics.addSpring(s2)

    z += 1 #increment 'z'


    #Draw springs
    for s in physics.springs:
        py5.line(s.a.x(), s.a.y(), s.b.x(), s.b.y())
py5.run_sketch()
