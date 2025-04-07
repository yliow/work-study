n = 2
while 1:
    p = 1
    for i in range(1, n):
        p *= (1 - i / 366.0)
    print(n, 1 - p)
    if 1 - p > 0.5:
         break
    n += 1