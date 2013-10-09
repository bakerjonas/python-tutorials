#!/usr/bin/env python
"""Usage:
  pimp.py blur [options] <infile> 
  pimp.py sharp [options] [--alpha=<int>] <infile> 

Options:
    -h, --help                      Show this screen
    -v, --version                   Program version
    -f <int>, --factor=<int>    Factor for operation.
"""
from docopt import docopt
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage

def main():
    "Parse command line and dispatch"
    args = docopt(__doc__, version='pimp 1.0')
    
    fname = args['<infile>']
    img = misc.imread(fname) 

    if '--factor' in args:
        fac = int(args['--factor'])
    else:
        fac = 1

    if args['blur']: 
        img = do_blur(img, fac)
    elif args['sharp']: 
        if '--alpha' in args:
            alpha = int(args['--alpha'])
        else:
            alpha = 1
        img = do_sharp(img, fac, alpha)

    showtime(img)

def do_blur(img, fac):
    "Perform gaussian blur on image and return"
    return ndimage.gaussian_filter(img, fac)

def do_sharp(img, fac, alpha):
    "Apply sharpening filter on blurred image"
    filtered = ndimage.gaussian_filter(img, fac)
    sharpened = img + alpha * (img - filtered)
    return sharpened

def showtime(img):
    "Image, flaunt it!"
    plt.imshow(img, cmap=plt.cm.gray)
    plt.show()

if __name__ == '__main__':
    main()
