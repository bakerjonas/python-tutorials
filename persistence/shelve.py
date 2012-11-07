import shelve
from convenience import parseWorkshop

SHELF_FILE = "shelf.dat"

def listShelf(shelf):
    for key in shelf.keys():
        print key
    print

def initializeShelf():
    workshops = parseWorkshop()

    f = shelve.open(SHELF_FILE)
    for w in workshops:
        f[w.name] = w
    f.close()

def initialize2():
    workshops = parseWorkshop()

    f = shelve.open(SHELF_FILE, writeback=True)
    f['workshops'] = []
    f['participants'] = []
    for w in workshops:
        f['workshops'].append(w.name)
        for p in w.participants:
            f['participants'].append(p.asTuple())
    f.close()


def shelf_example():
    initializeShelf()

    f = shelve.open(SHELF_FILE)
    listShelf(f)

    workshop = f['Workshop 2012']
    workshop.printWorkshop()

    f.close()

if __name__ == '__main__':
    shelf_example()