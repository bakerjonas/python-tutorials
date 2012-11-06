from cheese.cheese import Cheese  # Import the base class

class Gouda(Cheese):
    def __init__(self, weight = 1):  
        """This is the object constructor

        Constructors are automatically called when new objects (cheeses) are
        created (produced).
        """
        self.name = "Gouda"
        self.nholes = weight * 10
        self.taste = "gouda"

def holes():
    cheese = Gouda()
    return cheese.holes()
