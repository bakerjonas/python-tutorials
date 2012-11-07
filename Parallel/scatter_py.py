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
    data = [(i+1)**2 for i in xrange(size)]
else:
   data = None

print 'foo ', rank, data

data = comm.scatter(data, root=0)
print 'rank=', rank, data
data += 100
data = comm.gather(data, root=0)

print 'rank=', rank, data
