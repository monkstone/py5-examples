import py5
import numpy as np

def settings():
    py5.size(480, 320)

def setup():
    s = 300  # Scale.
    n = py5.width
    m = py5.height
    x = np.linspace(-n / s, n / s, num=n).reshape((1, n))
    y = np.linspace(-m / s, m / s, num=m).reshape((m, 1))
    Z = np.tile(x, (m, 1)) + 1j * np.tile(y, (1, n))

    C = np.full((m, n), -0.4 + 0.6j)
    M = np.full((m, n), True, dtype=bool)
    N = np.zeros((m, n))
    for i in range(255):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        N[M] = i
    py5.set_np_pixels(N, bands='L')

py5.run_sketch()
