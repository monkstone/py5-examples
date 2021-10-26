import py5
from vec2d import vec2d
# taste of noise 7 by leon denise 2021/10/14
# result of experimentation with organic patterns
# using code from Inigo Quilez, David Hoskins and NuSan
# thanks to Fabrice Neyret for code reviews
# licensed under hippie love conspiracy
def settings():
    py5.full_screen(py5.P2D)

def setup():
    global wrapper, img, previous_time, last_mouse_position, mouse_click_state, start
    sketch_title('Taste Of Noise 7')
    previous_time = 0.0
    mouse_dragged = False
    mouse_click_state = 0.0
    last_mouse_position = vec2d.Vec2D(py5.mouse_x, py5.mouse_y)
    wrapper = py5.load_shader('shaders/data/taste_of_noise7.glsl')
    img = py5.load_shader('shaders/data/image.glsl')
    # Assume the dimension of the window will not change over time
    wrapper.set('iResolution', py5.width, py5.height, 0.0)
    start = py5.millis()


def draw():
    global last_mouse_position
    wrapper.set('iTime', playback_time_seconds())
    previous_time = playback_time_seconds()
    img.set('iChannel0', py5.get())
    # mouse pixel coords. xy: current (if MLB down), zw: click
    if py5.is_mouse_pressed:
        last_mouse_position = vec2d.Vec2D(py5.mouse_x, py5.mouse_y)
        mouse_click_state = 1.0
    else:
        mouse_click_state = 0.0

    wrapper.set('iMouse', last_mouse_position.x, last_mouse_position.y, mouse_click_state, mouse_click_state)
    py5.shader(wrapper)
    # Draw the output of the shader onto a rectangle that covers the whole viewport.
    py5.rect(0, 0, py5.width, py5.height)

def playback_time_seconds():
    return (py5.millis() - start) / 1000.0

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
