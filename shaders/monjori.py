##
# Monjori.
#
# GLSL version of the 1k intro Monjori from the demoscene
# (http://www.pouet.net/prod.php?which=52761)
# Ported from the webGL version available in ShaderToy:
# http://www.iquilezles.org/apps/shadertoy/
# (Look for Monjori under the Plane Deformations Presets)
import py5
import os

def setup():
    global monjori
    sketch_title('Monjori')
    py5.no_stroke

    monjori = py5.load_shader('shaders/data/monjori.glsl')
    monjori.set('resolution', py5.width, py5.height)


def draw():
    monjori.set('time', py5.millis() / 1000.0)
    py5.shader(monjori)
    # This kind of effects are entirely implemented in the
    # fragment shader, they only need a quad covering the
    # entire view area so every pixel is pushed through the
    # shader.
    py5.rect(0, 0, py5.width, py5.height)


def settings():
    py5.size(640, 360, py5.P2D)

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
