#!/usr/bin/env python
#!/usr/bin/env python

def integrate_f(a, b, N):
    f = lambda x: x**2-x
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx) 
    return s * dx


