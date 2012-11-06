class Cheese(object):
    """Simple cheese base class
    
    A base class provides common functionality to classes which inherit from
    it.
    """
    def __str__(self):
        """Return a string representation of the object for printing"""
        return "{0} tastes like {1}.".format(self.name, self.taste)

    def holes(self):
        """Return a list of holes in the cheese"""
        return range(self.nholes)
