def func(default=[]):
    return default

result = func()
result.append(1)
result1 = func()

if result == result1:
    print  'I got you'
else:
    print 'Argh!'
