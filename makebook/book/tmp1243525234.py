def a(n):
    if n in [0, 1]: return 1
    else:
        return 2 * a(n/2) + 1
def b(n):
    if n in [0, 1]: return 1
    else:
        return 2 * b(round(n/2.0)) + 1

for n in range(0, 9):
    print(n, a(n), b(n))

for n in range(100000, 100011):
    print(n, float(a(n))/float(b(n)))