from math import sqrt

def an(n):
    if n == 0: return 3
    elif n == 1: return 5
    else: return an(n - 1) + an(n - 2)

def bn(n):
    r = sqrt(5)
    r1 =  (-1 + r) / 2
    r2 =  (-1 - r) / 2
    A = (-3 - 2 * r1) * sqrt(5) / 5 
    B = (3 + 2 * r2) * sqrt(5)/ 5
    return -A/r1 ** (n + 1) - B/r2 ** (n + 1)  

for n in range(10):
    print(an(n), bn(n))
