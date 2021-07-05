import py5
VerletPhysics3D = py5.JClass('toxi.physics3d.VerletPhysics3D')
VerletParticle3D = py5.JClass('toxi.physics3d.VerletParticle3D')
VerletSpring3D = py5.JClass('toxi.physics3d.VerletSpring3D')
AttractionBehavior2D = py5.JClass('toxi.physics3d.behaviors.AttractionBehavior3D')
Vec2D = py5.JClass('toxi.geom.Vec3D')
PeasyCam = py5.JClass('peasy.PeasyCam')

from collections import defaultdict
from itertools import chain



W, H = 1400, 800

####### Multiple relations example (see part 2.7)
####### -> https://www.wolframphysics.org/technical-introduction/basic-form-of-models/rules-depending-on-more-than-one-relation/

# RULE (if edges corresponding to pattern 'a' -> replace by new edges corresponding to pattern 'b')
a = [[0, 1], [0, 2]]
b = [[0, 2], [0, 3], [1, 3], [2, 3]]


# Starting axiom
s = [[0, 0], [0, 0]]


# Number of steps/generations
G = 13



def settings():
    py5.size(W, H, py5.P3D)

def setup():
    py5.stroke(105, 140, 200)
    py5.smooth(8)

    global physics, uniques, a, b, s

    cam = PeasyCam(py5.get_current_sketch(), 1000)
    physics = VerletPhysics3D()
    physics.setDrag(.2)


    #Transform / Translate axiom according to rule
    a_,b_,s_ = [list(chain(*e)) for e in (a,b,s)]
    ws = set(k for k in b_ if k > max(a_))

    while ws:
        a_ += [ws.pop()]
        s_ += [max(s_)+1]

    d = {k:i for i, k in enumerate(a_)}
    axiomt = lambda x, y = _s, z = y: y[z[x]]
    t = [axiomt for e in b]
    print("Translated axiom: ", t)

    #Finding matching relations in the array of edges
    for g in range(G-1):
        temp = []
        ids = set()
        w = max(chain(*t))+1

        #This part (until line 66 + line 70) should be modified depending on the input rule
        for i, (xa, ya) in enumerate(t):
            for j, (xb, yb) in enumerate(t):
                if i != j:
                    if xa == xb and yb > ya: # reminder: [[xa, xb], [ya, yb]] = [[0, 1], [0, 2]]
                        if {i, j}.isdisjoint(ids):
                            temp.append((xa, ya, xb, yb))
                            ids.update([i, j])

        for id in sorted(ids, reverse=True): del t[id]

        for xa, ya, xb, yb in temp[::-1]:
            t.extend([[xa, yb], [xa, w], [ya, w], [yb, w]])
            w += 1



    #Get id of each node
    uniques = list(set(chain(*t)))

    print("Hypergraph after %.i steps: %.i nodes // %.i edges" % (G, len(uniques), len(t)))

    #Store neighboring nodes for each node in a dictionary (handle both binary and ternary edges)
    d = defaultdict(set)
    for edge in t:
        n = len(edge)
        if n == 2:
            n1, n2 = edge
            d[n1].add(n2)
            d[n2].add(n1)
        elif n == 3:
            n1, n2, n3 = edge
            d[n1].add(n2)
            d[n3].add(n2)
            d[n2].update([n1, n3])
        else:
            pass

    #Find smallest and largest number of neighbors (not mandatory, using this for computing edge length later)
    nn = sorted(len(d[k]) for k in d)
    lo, hi = nn[0], nn[-1]+1


    #Create a particle for each node + give it a repulsion force
    for n in uniques:
        p = VerletParticle3D(Vec3D.randomVector().scale(W).add(Vec3D(W>>1, H>>1, 0)))
        physics.addParticle(p)
        physics.addBehavior(AttractionBehavior3D(p, 200, -.5))


    #Create spring between each pair of nodes (handle both binary and ternary edges)
    for edge in t:
        n = len(edge)
        if n == 2:
            n1, n2 = edge
            p1, p2 = [physics.particles.get(uniques.index(n)) for n in edge]
            l = ( len(d[n1]) + len(d[n2]) ) * .5 # make length of edge depend on the average number of neighbors of its end vertices
            f = py5.remap(l, lo, hi, 1, .3) #the higher the degree of the end vertices, the lower the factor
            s = VerletSpring3D(p1, p2, l*l*f, .3)
            physics.addSpring(s)
        elif n == 3:
            n1, n2, n3 = edge
            p1, p2, p3 = [physics.particles.get(uniques.index(n)) for n in edge]
            l1 = ( len(d[n1]) + len(d[n2]) ) * .5
            l2 = ( len(d[n2]) + len(d[n3]) ) * .5
            f1 = py5.remap(l1, lo, hi, 1, .2)
            f2 = py5.remap(l2, lo, hi, 1, .2)
            s1 = VerletSpring3D(p1, p2, l1*l1*f1, .2)
            s2 = VerletSpring3D(p2, p3, l2*l2*f2, .2)
            physics.addSpring(s1)
            physics.addSpring(s2)
        else:
            pass

def draw():
    py5.background(255)
    py5.translate(-W>>1, -H>>1)

    #Update physics
    physics.update()

    #Draw springs
    for s in physics.springs:
        py5.line(s.a.x(),s.a.y(), s.a.z(), s.b.x(), s.b.y(), s.b.z())

    #Draw nodes
    py5.push_style()
    py5.stroke_weight(3.5)
    py5.stroke(190, 240, 255)
    for p in physics.particles:
        py5.point(p.x(), p.y(), p.z())
    py5.pop_style()

py5.run_sketch()
