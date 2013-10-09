"""
This is a file-level docstring:

* It should document general features of the module contained in the file
* Perhaps even who to blame for it

"""

def hello():
    """
    This function says "Hello world", no more, no less.
    """
    print "Hello world"

def world():
    """
    This function prints the toplevel docstring, and the the hello()
    docstring.
    """
    print '-=' * 25
    print __doc__

    print '-+' * 25
    print hello.__doc__

if __name__ == '__main__':
    hello()
    world()

