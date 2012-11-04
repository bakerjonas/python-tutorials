def fib2(n = 1000): 
    """Print a Fibonacci series up to n. Default: n = 1000."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    # Return multiple values (as tuple)
    return result, a, b    

x = fib2()
r, a, b = fib2()
print x
print a, b

