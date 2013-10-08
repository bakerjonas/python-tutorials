"""Usage:
  pimp.py blur [options] <infile> 
  pimp.py sharp [options] <infile> 

Options:
    -h, --help                      Show this screen
    -v, --version                   Program version
    -f <float>, --factor=<float>    Factor for operation.
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

    if 'fac' in args:
        fac = args['fac']
    else:
        fac = 1.0

    if args['blur']: 
        do_blur(img, fac)
    elif args['sharp']: 
        do_sharp(img, fac)

    showtime(img)

def do_blur(img, fac):
    "Perform gaussian blur on image and return"
    return ndimage.gaussian_filter(img, 3)

def do_sharp(img, fac):
    "Apply sharpening filter on blurred image"
    filtered = ndimage.gaussian_filter(img, 1.0)
    alpha = 30
    sharpened = img + alpha * (img - filtered)
    return sharpened

def showtime(img):
    "Image, flaunt it!"
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    main()
