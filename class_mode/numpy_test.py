from py5 import Sketch
import numpy as np

class NumpyTest(Sketch):

    def settings(self):
        self.size(100, 100)

    def setup(self):
        self.background(255, 0, 0)
        array = np.zeros((50, 50, 3), dtype=np.uint8)
        g = self.create_graphics(50, 50)
        g.begin_draw()
        g.set_np_pixels(array, bands='RGB') # could have use 'L' for grayscale
        g.end_draw()
        self.image(g, 25, 25)

numpy_test = NumpyTest()
numpy_test.run_sketch()
