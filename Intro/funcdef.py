def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.
    
    This is a long docstring.
    Here you can provide a detailed description.
    """
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

fib(100)
