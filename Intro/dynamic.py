def raboof(x, y=5):
    return x**y * raboof.foo
raboof.foo = 0.1

print(raboof(2))
