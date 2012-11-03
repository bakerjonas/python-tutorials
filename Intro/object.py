a = Foobar(1)
b = Foobar(42)
print(a, b )# invokes __str__()
print(b.double())
Foobar.bar = False # set global class variable
print(a, b)
