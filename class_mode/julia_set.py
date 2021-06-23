from py5 import Sketch

"""
JuliaSet
After a sketch by Alexandre Villares
"""

class JuliaSet(Sketch):
    def settings(self):
        self.size(640, 480)

    def setup(self):
        global cX, cY, maxIter
        cX = -0.7
        cY = 0.27015
        maxIter = 300

    def draw(self):
        self.load_pixels()
        for x in range(self.width):
            for y in range(self.height):
                zx = 1.5 * (x - self.width / 2) / (0.5 * self.width)
                zy = (y - self.height / 2) / (0.5 * self.height)
                i = maxIter
                while zx * zx + zy * zy < 4 and i > 0:
                    tmp = zx * zx - zy * zy + cX
                    zy = 2.0 * zx * zy + cY
                    zx = tmp
                    i -= 1
                self.color_mode(self.HSB)
                c = self.color(i / maxIter * 255, 255, 255 if i > 1 else 0)
                self.pixels[x + y *self.width] = c
        self.update_pixels()

julia = JuliaSet()
julia.run_sketch()
