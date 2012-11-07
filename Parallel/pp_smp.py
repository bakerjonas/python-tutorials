import pyquad
import pp

n = 4
start = -20.0
step = 10.0
server = pp.Server(n)

p = []
for i in range(n):
    a = start + i * step
    b = a + step
    p.append(server.submit(pyquad.integrate_f, (a, b, 1000)))

I = 0.0
for i in range(n):
    I += p[i]() 

print I, pyquad.integrate_f(-20.0, 20.0, 4000)
print server.print_stats()
