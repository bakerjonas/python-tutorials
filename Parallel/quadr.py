#!/usr/bin/env python
from mpi4py import MPI
import numpy
import sys
import pyquad

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 4
start = -20.0
step = 10.0

view = []

for i in range(n):
    a = start + i * step
    b = a + step
    view.append((a, b, 1000))

#print view

comm.bcast(view, root=0)

a, b, N = view[rank]
I = pyquad.integrate_f(a, b, N)

if rank == 0:
    comm.reduce(0.0, I, op=MPI.SUM, root=0)
    print I, pyquad.integrate_f(-20.0, 20.0, 4000)
else:
    comm.reduce(I, None, op=MPI.SUM, root=0)

