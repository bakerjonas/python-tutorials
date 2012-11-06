from cheese.cheese import Cheese  # Import the base class

class Maasdam(Cheese):
    def __init__(self, weight = 1):  
        """This is the object constructor

        Constructors are automatically called when new objects (cheeses) are
        created (produced).
        """
        self.name = "Maasdam"
        self.nholes = weight * 10
        self.taste = "mmm, ahh, ooh"

def holes():
    cheese = Maasdam()
    return cheese.holes()
