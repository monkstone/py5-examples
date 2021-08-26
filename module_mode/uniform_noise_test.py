import py5

UniformNoise = py5.JClass('micycle.uniformnoise.UniformNoise')
Color = py5.JClass('java.awt.Color')
OCTAVES = 4

def settings():
    py5.size(800, 800)

def setup():
    global unoise
    sketch_title('Uniform Noise Test')
    py5.noise_detail(OCTAVES)
    py5.load_pixels()
    unoise = UniformNoise()

def draw():
    global val
    for y in range(py5.height):
        for x in range(py5.width):
            if (x < py5.width / 2):
                val = (py5.noise(x * 0.015, y * 0.015, py5.frame_count * 0.1) + 1) / 2
            else:
                val = unoise.uniformNoise(x * 0.0085, y * 0.0085, py5.frame_count * 0.01, OCTAVES, 0.5)
            py5.pixels[y * py5.width + x] = Color.HSBtoRGB(val, 1, 1)
    py5.update_pixels()

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
