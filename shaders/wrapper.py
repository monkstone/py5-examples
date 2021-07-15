# uniform iChannelTime[4]         # channel playback time (in seconds)
# uniform vec3  iChannelResolution[4] # channel resolution (in pixels)
# uniform samplerXX iChannel0..3 # input channel. XX = 2D/Cube
import py5
from vec2d import vec2d

last_mouse_position = vec2d.Vec2D(0, 0)

def settings():
    py5.size(640, 360, py5.P2D)


def setup():
    global wrapper, previous_time, last_mouse_position, mouse_click_state, start
    sketch_title('Shadertoy Default Wrapper')
    previous_time = 0.0
    mouse_dragged = False
    mouse_click_state = 0.0
    last_mouse_position = vec2d.Vec2D(py5.mouse_x, py5.mouse_y)
    wrapper = py5.load_shader('shaders/data/default_shader.glsl')
    # Assume the dimension of the window will not change over time
    wrapper.set('iResolution', py5.width, py5.height, 0.0)
    start = py5.millis()


def playback_time_seconds():
    return (py5.millis() - start) / 1000.0


def render_time():
    return playback_time_seconds() - previous_time


def draw():
    global last_mouse_position
    wrapper.set('iTime', playback_time_seconds())
    wrapper.set('iDeltaTime', render_time())
    previous_time = playback_time_seconds()
    # shader playback frame
    wrapper.set('iFrame', py5.frame_count)
    # mouse pixel coords. xy: current (if MLB down), zw: click
    if py5.is_mouse_pressed:
        last_mouse_position = vec2d.Vec2D(py5.mouse_x, py5.mouse_y)
        mouse_click_state = 1.0
    else:
        mouse_click_state = 0.0

    wrapper.set('iMouse', last_mouse_position.x, last_mouse_position.y, mouse_click_state, mouse_click_state)
    # Set the date
    # Note that iDate.y and iDate.z contain month-1 and day-1 respectively,
    # while x does contain the year (see: https://www.shadertoy.com/view/ldKGRR)

    wrapper.set('iDate', py5.year() + 1990, py5.month() - 1, py5.day() - 1, py5.second() )
    # This uniform is undocumented so I have no idea what the range is
    wrapper.set('iFrameRate', py5.get_frame_rate())
    py5.shader(wrapper)
    # Draw the output of the shader onto a rectangle that covers the whole viewport.
    py5.rect(0, 0, py5.width, py5.height)

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
