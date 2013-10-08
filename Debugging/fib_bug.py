def fib2(n = 1000):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = a, a+b
    return result, a, b

if __name__ == '__main__':
    print fib2(10)
