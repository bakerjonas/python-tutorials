import cheese.dutch.maasdam
n = 0
for i in cheese.dutch.maasdam.holes(): n += 1

from cheese.dutch import maasdam
for i in maasdam.holes(): n += 1

from cheese.dutch.maasdam import holes
#from cheese.dutch.maasdam import *
for i in holes(): n += 1

print n
