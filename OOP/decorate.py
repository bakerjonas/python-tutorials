def twoTimes(h):
    return lambda x: 2 * h(x)

@twoTimes
def f(x):
    return x**2

print f(5)
