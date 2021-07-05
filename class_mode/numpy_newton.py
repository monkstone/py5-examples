import py5
import numpy as np
import cmath

def func(z):
    return z*(z*z*z*z*z*z - 1.0)


global xa, xb, ya, yb, maxIt, h, s
xa, xb, ya, yb = -2.0, 2.0, -2.0, 2.0
maxIt, h, s = 20, 1e-6, 1e-3

def settings():
    py5.size(512, 512)

def setup():
    n = py5.width
    m = py5.height
    x = np.linspace(-n / s, n / s, num=n).reshape((1, n))
    y = np.linspace(-m / s, m / s, num=m).reshape((m, 1))
    Z = np.tile(x, (m, 1)) + 1j * np.tile(y, (1, n))
    zy = y*(yb - ya)/(n - 1) + ya
    zx = x*(xb - xa)/(m - 1) + xa
    C = np.full((m, n), complex)
    M = np.full((m, n), True, dtype=bool)
    N = np.zeros((m, n, 3), dtype=np.uint8)
    for i in range(255):
        dz = (func(z + complex(h, h)) - func(z))/complex(h, h)
        if dz != 0: Z0 = z - func(Z)/dz
        if abs(z0 - Z) < eps: break
        Z = Z0
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z0 - Z) > 20] = False
        N[M] = [i%5*64, i%17*16, i%9*32]
    py5.set_np_pixels(N, bands='RGB')
py5.run_sketch()
