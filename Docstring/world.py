"""
This is a file-level docstring:

* It should document general features of the module contained in the file
* Perhaps even who to blame for it
"""

class World(object):
    """
    Here we document the main purpose of the class.
    """
    def hello(self):
        """
        This function says "Hello world", no more, no less.
        """
        print "Hello world"

    def world(self):
        """
        This function prints the toplevel docstring, and the the hello()
        docstring.
        """
        print '-=' * 25
        print __doc__

        print '-+' * 25
        print self.hello.__doc__
        print World.hello.__doc__

if __name__ == '__main__':
    o = World()
    o.hello()
    o.world()
    print '~~' * 25
    print World.__doc__

