#!/usr/bin/env python
from mpi4py import MPI
import numpy as np
from scipy.integrate import quad
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

ival = (-20.0, 20.0)
step = sum(map(abs, ival))/size

view = None
if rank == 0:
    foo = lambda i: (ival[0] + i * step, ival[0] + (i + 1) * step)
    view = [ foo(i) for i in range(size)]

# silly: scatter is better, but utilizing rank is best
view = comm.bcast(view, root=0) 

f = lambda x: math.exp(-0.1*x**2)
a, b = view[rank]
I = quad(f, a, b)[0]

if rank == 0:
    I = comm.reduce(0.0, I, op=MPI.SUM, root=0)
    print I, quad(f, -20.0, 20.0)[0]
else:
    comm.reduce(I, None, op=MPI.SUM, root=0)

