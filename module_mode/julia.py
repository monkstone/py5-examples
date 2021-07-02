import py5
import numpy as np

def settings():
    py5.size(480, 320)

def setup():
    sketch_title('Julia Set')
    s = 300  # Scale.
    n = py5.width
    m = py5.height
    x = np.linspace(-n / s, n / s, num=n).reshape((1, n))
    y = np.linspace(-m / s, m / s, num=m).reshape((m, 1))
    Z = np.tile(x, (m, 1)) + 1j * np.tile(y, (1, n))

    C = np.full((m, n), -0.4 + 0.6j)
    M = np.full((m, n), True, dtype=bool)
    N = np.full((m, n, 3), [0, 0, 100], dtype=np.uint8)
    for i in range(127):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        N[M] = [i * 2, 0, 100]
    py5.set_np_pixels(N, bands='RGB')

def sketch_title(title):
    py5.get_surface().set_title(title)

py5.run_sketch()
