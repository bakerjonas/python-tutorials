# Often we need an index, as well as a value:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

# Looping over two sets of values:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

# Looping backwards:
for i in reversed(range(1,10,2)):
    print i

# List comprehensions:
print [ i for i in range(8) if i % 2] 
