def f(x):
    s = 0
    for n in range(100):
        s += (2**n + (-1)**n) / 3**n * x**n
    return s

def g(x):
    return (18 - 3 * x) / (9 - 3 * x - 2 * x * x)


for x in range(10):
    x = x / 100
    print(f(x), g(x))
