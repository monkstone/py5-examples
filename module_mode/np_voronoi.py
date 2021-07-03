import py5
import numpy as np
# sketch inspired by dorverbin
# https://stackoverflow.com/questions/53696900/render-voronoi-diagram-to-numpy-array
# and yes one-hot coding is a thing
def settings():
    py5.size(400,  300)

def setup():
    sketch_title('Fast Voronoi')
    n = py5.random_int(30, 50)
    cx = np.random.randint(py5.width, size=(n))
    cy = np.random.randint(py5.height, size=(n))
    X, Y = np.meshgrid(np.arange(py5.width), np.arange(py5.height))
    squared_dist = (X[:, :, np.newaxis] - cx[np.newaxis, np.newaxis, :]) ** 2 + \
                   (Y[:, :, np.newaxis] - cy[np.newaxis, np.newaxis, :]) ** 2
    indices = np.argmin(squared_dist, axis=2)
    # Convert the previous 2D array to a 3D array where the extra dimension is a one-hot
    # encoding of the index
    one_hot_indices = indices[:, :, np.newaxis, np.newaxis] == np.arange(cx.size)[np.newaxis, np.newaxis, :, np.newaxis]
    # Create a random color for each center
    colours = np.random.randint(255, size=(n, 3), dtype=np.uint8)
    voronoi = (one_hot_indices * colours[np.newaxis, np.newaxis, :, :]).sum(axis=2)
    py5.set_np_pixels(voronoi, bands='RGB')

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
