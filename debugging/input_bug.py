def input_example():
    a = raw_input('Enter a number: ')

    if a > 0:
        print 'Positive'
    elif a == 0:
        print 'Null'
    elif a < 0:
        print 'Negative'

if __name__ == '__main__':
    input_example()