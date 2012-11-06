from cheese.cheese import Cheese  # Import the base class

class Emmental(Cheese):
    def __init__(self, weight = 1):  
        """This is the object constructor

        Constructors are automatically called when new objects (cheeses) are
        created (produced).
        """
        self.name = "Emmental"
        self.nholes = weight * 10
        self.taste = "Maasdam"

def holes():
    cheese = Emmental()
    return cheese.holes()
