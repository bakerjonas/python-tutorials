def stateful(x):
    x = x + 1
    y = x + 1
    if y > x: return False
    return True
