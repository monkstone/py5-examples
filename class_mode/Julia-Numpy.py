import py5
import numpy as np

def settings():
    py5.size(1000, 1000)

def setup():
    x_dim = py5.width
    y_dim = py5.height
    x_min = -1.8
    x_max = 1.8
    y_min = -1.8j
    y_max = 1.8j
    z = np.zeros((y_dim,x_dim),dtype='complex128')
    c = -0.4+.6j
    for l in range(y_dim):
        z[l] = np.linspace(x_min,x_max,x_dim) -np.linspace(y_min,y_max,y_dim)[l]
    it = 0
    max_iter = 300
    while(it < max_iter):
        z[np.absolute(z) < 10] = z[np.absolute(z) < 10]**2 + c #the logic in [] replaces our if statement. This line
        it += 1                                                #updates the whole matrix at once, no need for loops!
    py5.set_np_pixels(z, bands='L')

py5.run_sketch()
