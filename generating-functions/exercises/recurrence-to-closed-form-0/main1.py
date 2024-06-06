from math import sqrt

def bn(n):
    if n == 0: return 3
    elif n == 1: return 5
    else: return 7 * bn(n - 1) + 11 * bn(n - 2)

def cn(n):
    r = sqrt(93)
    r1 =  (-7 + r) / 22
    r2 =  (-7 - r) / 22
    A = (-3 + 16*r1) * sqrt(93) / 93 
    B = (3 - 16 * r2) * sqrt(93)/ 93
    return -A/r1 ** (n + 1) - B/r2 ** (n + 1)  

for n in range(10):
    print(bn(n), cn(n))
