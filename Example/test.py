"""
Test suite for the imp program.
"""
import pimp
import unittest
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage

class TestImpFunctions(unittest.TestCase):
    def setUp(self):
        self.img = misc.lena()

    def test_blur(self):
        img = pimp.do_blur(self.img, 0.0)
        self.assertTrue((img == self.img).all())

    def test_sharpen(self):
        img = pimp.do_sharp(self.img, 1.0)
        self.assertTrue((img != self.img).any())

if __name__ == '__main__':
    unittest.main()
