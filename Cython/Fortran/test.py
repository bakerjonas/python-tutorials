#!/usr/bin/env python
from __future__ import division
import sys
sys.path.append('@MAKE_BINARY_DIR@')

import numpy as np
from pygfunc import f
import matplotlib.pyplot as plt

c = f(0.1)
plt.pcolormesh(c)
plt.show()
