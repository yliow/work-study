def f(x):
    s = 0.0
    for n in range(100):
        s += (1.0/4**n) * x**n
    return s

def g(x):
    s = 0.0
    for n in range(100):
        s += (2.0/3)**n * x**n
    return s

def h(x):
    s = 0.0
    for n in range(100):
        s += ((-3.0/5) * (1.0/4)**n + (8.0/5) * (2.0/3)**n) * x**n
    return s

for x in range(10):
    x = x/ 100
    print(f(x) * g(x), h(x))
