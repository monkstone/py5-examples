import py5
Capture = py5.JClass('processing.video.Capture')

def settings():
    py5.size(1280, 960, py5.P2D)


def setup():
    global cam, my_filter
    # sketch_title 'Droste'
    my_filter = py5.load_shader('data/droste.glsl')
    my_filter.set('resolution', py5.width, py5.height)
    cam = Capture(py5.get_current_sketch(), "UVC Camera (046d:0825)")
    cam.start()


def draw():
    cam.read()
    py5.background(0)
    py5.image(cam, 0, 0, py5.width, py5.height)
    my_filter.set('frameCount', py5.frame_count)
    if (py5.is_mouse_pressed):
        return
    py5.apply_filter(my_filter)

py5.run_sketch()
