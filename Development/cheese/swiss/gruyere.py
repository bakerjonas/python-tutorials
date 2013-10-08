from cheese.cheese import Cheese  # Import the base class

class Gruyere(Cheese):
    def __init__(self, weight = 1):  
        """This is the object constructor

        Constructors are automatically called when new objects (cheeses) are
        created (produced).
        """
        self.name = "Gruyere"
        self.nholes = weight * 10
        self.taste = "oh yes, ohh yeah"

def holes():
    cheese = Gruyere()
    return cheese.holes()
