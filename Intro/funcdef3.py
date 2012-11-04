def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    """Ask the user a question and validate it."""
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

try:
    ask_ok("Do you want some cheese? ", 2)
except IOError as err:
    print "Error: ", err
finally:
    print "Goodbye."
