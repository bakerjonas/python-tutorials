#!/usr/bin/env python
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# pass explicit MPI datatypes
if rank == 0:
   data = [ "foo" for i in range(5) ] 
   comm.send(data, dest=1, tag=77)
elif rank == 1:
   data = comm.recv(source=0, tag=77)
   print data
