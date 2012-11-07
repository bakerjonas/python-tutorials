class Cheese:
    def taste(self):
        return self.palate  # Does not exist yet!
    
    def holes(self):
        return 0

class Emmental(Cheese):
    def __init__(self, taste="good", smell="bad"):  
        self.palate = taste
        self.nose = smell
        
    def holes(self):
        self.n = 10     # Add class variables dynamically
        return self.n
        
    def smell(self):
        return self.nose

ost = Emmental(smell="horror")
ost.n = 100
print ost.holes(), ost.taste(), ost.smell()
