from py5 import Sketch
import cmath

def func(z):
    return z*(z*z*z*z*z*z - 1.0)

class Newton(Sketch):
    global xa, xb, ya, yb, maxIt, h, eps
    xa, xb, ya, yb = -2.0, 2.0, -2.0, 2.0
    maxIt, h, eps = 20, 1e-6, 1e-3

    def settings(self):
        self.size(512, 512)

    def draw(self):
        self.load_pixels()
        for y in range(self.height):
            zy = y*(yb - ya)/(self.height - 1) + ya
            for x in range(self.width):
                zx = x*(xb - xa)/(self.width - 1) + xa
                z = complex(zx, zy)
                for i in range(maxIt):
                    dz = (func(z + complex(h, h)) - func(z))/complex(h, h)
                    if dz != 0: z0 = z - func(z)/dz
                    if abs(z0 - z) < eps: break
                    z = z0
                loc = x + y * self.width
                self.pixels[loc] = self.color(i%5*64, i%17*16, i%9*32)

        self.update_pixels()
        print(self.millis())

newton = Newton()
newton.run_sketch()
