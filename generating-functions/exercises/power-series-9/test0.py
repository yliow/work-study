def f(x):
    return 2.0 / (5 * x**4 - 7)

def g(x):
    s = 0
    for n in range(100):
        s += (-2.0/7)  * (5.0/7)**n * x**(4*n)
    return s

for x in range(11):
    x = x / 10
    print(f(x), g(x))
