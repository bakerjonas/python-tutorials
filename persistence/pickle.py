# -*- coding: utf-8 -*-

from convenience import parseWorkshop
import pickle
#import cPickle as pickle

PICKLE_FILE = 'pickle.dat'
class Pickler(object):
    @staticmethod
    def pickle1():
        workshops = parseWorkshop()
        with open(PICKLE_FILE, 'wb') as f:
            pickle.dump(workshops, f)


    @staticmethod
    def pickle2():
        workshops = parseWorkshop()

        with open(PICKLE_FILE, 'wb') as f:
            for w in workshops:
                pickle.dump(w.name, f)
                for p in w.participants:
                    pickle.dump(p.asTuple(), f)

def pickle_example1():
    Pickler.pickle1()
    with open(PICKLE_FILE, 'rb') as f:
        workshops = pickle.load(f)

    for w in workshops:
        w.printWorkshop()

def pickle_example2():
    Pickler.pickle2()
    content = []
    with open(PICKLE_FILE, 'rb') as f:
        while True:
            try:
                content.append(pickle.load(f))
            except EOFError:
                print "Unpickled %i objects." % len(content)
                break

    for c in content:
        print c


if __name__ == '__main__':
    pickle_example2()