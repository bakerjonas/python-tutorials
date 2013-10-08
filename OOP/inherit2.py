class Cheese:
    def taste(self):
        return "good"
    
    def holes(self):
        return 0

class Emmental(Cheese):
    def __init__(self, hole_list):
        self.myholes = hole_list

    def holes(self):
        return self.count_holes()

    def smell(self):
        return "sour"

    def count_holes(self):
        return len(self.myholes)

class Brunost(Cheese):
    def smell(self):
        return "brown"

    def taste(self):
        return "brown"

def say_cheese(ost):
    return "Cheese: {0} {1} {2}".format(ost.holes(), ost.taste(), ost.smell())

emmen = Emmental([1, 1, 1, 1])
brun = Brunost()
print emmen.holes(), emmen.taste(), emmen.smell()
print say_cheese(emmen)
print say_cheese(brun)

