from math import sqrt

def an(n):
    if n == 0: return 3
    elif n == 1: return 5
    else: return an(n - 1) + an(n - 2)

def a(x, N=20):
    s = 0
    for n in range(N + 1):
        s += an(n) * x**n
    return s

def a1(x): # rational express
    return (-3 - 2 * x) / (x**2 + x - 1)

def a2(x): # partial fractions
    r = sqrt(5)
    r1 =  (-1 + r) / 2
    r2 =  (-1 - r) / 2
    A = (-3 - 2 * r1) * sqrt(5) / 5 
    B = (3 + 2 * r2) * sqrt(5) / 5
    return A / (x - r1) + B / (x - r2)

for x in range(0, 10):
    x = x / 100.0
    print(a(x), a1(x), a2(x))
    
