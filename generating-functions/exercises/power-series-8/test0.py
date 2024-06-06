def f(x):
    return 1.0 / (3 + 5 * x**4)

def g(x):
    s = 0
    for n in range(100):
        s += (-1)**n * (1.0/3) * (5.0/3)**n * x**(4*n)
    return s

for x in range(9):
    x = x / 10
    print(f(x), g(x))
