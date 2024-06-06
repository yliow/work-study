from math import sqrt

def bn(n):
    if n == 0: return 3
    elif n == 1: return 5
    else: return 7 * bn(n - 1) + 11 * bn(n - 2)

def b(x, N=20):
    s = 0
    for n in range(N + 1):
        s += bn(n) * x**n
    return s

def b1(x): # rational express
    return (-3 + 16 * x) / (11 * x**2 + 7 * x - 1)

def b2(x): # partial fractions
    r = sqrt(93)
    r1 =  (-7 + r) / 22
    r2 =  (-7 - r) / 22
    A = (-3 + 16 * r1) * sqrt(93) / 93 
    B = (3 - 16 * r2) * sqrt(93) / 93
    return A / (x - r1) + B / (x - r2)

for x in range(0, 10):
    x = x / 100.0
    print(b(x), b1(x), b2(x))
    
