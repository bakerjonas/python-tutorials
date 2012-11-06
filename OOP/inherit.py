class Cheese:
    def taste(self):
        return "good"
    def holes(self):
        return 0

class Emmental(Cheese):
    def holes(self):
        return 10
    def smell(self):
        return "sour"

ost = Emmental()
print ost.holes(), ost.taste(), ost.smell()

