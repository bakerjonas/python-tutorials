class Cheese:
    def taste(self):
        return self.palate
    
    def holes(self):
        return 0

class Emmental(Cheese):
    def __init__(self, taste, smell="bad"):
        self.palate = taste
        self.nose = smell
        
    def holes(self):
        self.n = 10
        return self.n
        
    def smell(self):
        return self.nose

ost = Emmental("exquisit")
ost.n = 100
print ost.holes(), ost.taste(), ost.smell()
