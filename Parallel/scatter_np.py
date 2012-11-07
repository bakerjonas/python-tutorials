#!/usr/bin/env python
#
# Simple scatter-gather example using mpi4py
#
# $ mpirun -np 4 python ./foo.py
#
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = np.arange(0.0, 40.0)
else:
   data = np.array()

print 'foo ', rank, data

data = comm.Scatter([data, MPI.DOUBLE], root=0)
#print 'rank=', rank, data
#data = data + 100
data = comm.Gather([data, MPI.DOUBLE], root=0)

#print 'rank=', rank, data
