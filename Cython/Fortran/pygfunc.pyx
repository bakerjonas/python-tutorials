cimport numpy as cnp
import numpy as np

cdef extern from "pygfunc.h":
    void c_gfunc(double, int, int, double *, double *, double *)

def f(float x, a=-10.0, b=10.0, n=100):
    cdef cnp.ndarray ax, c
    ax = np.arange(a, b, (b-a)/float(n))
    n = ax.shape[0]
    c = np.ndarray((n,n), dtype=np.float64, order='F')
    c_gfunc(x, n, n, <double *> ax.data, <double *> ax.data, <double *> c.data)
    return c

