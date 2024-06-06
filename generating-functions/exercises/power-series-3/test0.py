def f(x):
    return 1 + 2 * x + 2 / (3 + 4 * x) + 5 / (7 * x - 1)

def g(x):
    s = (-10/3) - (305/9) * x
    for n in range(2, 100):
        s += ((-1)**n * (2/3) * (4/3)**n - 5 * 7**n) * x**n
    return s

for x in range(10):
    x = x / 100
    print(f(x), g(x))
