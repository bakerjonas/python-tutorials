#
#
"""
Simple bug.
"""

class Apa(object):
    """
    yo yo
    """
    def fib2(self, n = 1000):
        """
        Hey hey
        """
        print self.fib2.__doc__, Apa.__doc__
        a, b = 0, 1
        result = []
        while a < n:
            result.append(a)
            a, b = a, a+b
        return result, a, b

if __name__ == '__main__':
    Apa().fib2()
