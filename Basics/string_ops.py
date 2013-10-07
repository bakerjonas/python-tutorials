>>> word = 'Foo' + 'Bar'
>>> '<' + word*2 + '>'
'<FooBarFooBar>'

>>> word[4]
>>> word[0:2]
>>> word[2:4]

>>> word[-1]     # The last character
>>> word[-2]     # The last-but-one character
>>> word[-2:]    # The last two characters
>>> word[:-2]    # Everything except the last two characters
>>> word[10:100] # Empty string
>>> word[-100:]  # FooBar
>>> word[-10]    # Error

>>> word[0] = 'x'  # Strings are immutable
