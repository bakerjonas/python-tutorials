a, b = 0, 1

while b < 1000:
    if a >= 500:
        break
    if a == 377:
        print
    if a > 300:
        a += 10
        print('All work and no play ')
        continue
    print b,
    a, b = b, a+b

