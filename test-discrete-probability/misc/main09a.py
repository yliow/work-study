# file: main09a.py
import random; random.seed()
count = 0
n = 1000000
for _ in range(n):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    c = random.randrange(1, 7)
    d = random.randrange(1, 7)
    e = random.randrange(1, 7)
    xs = [a, b, c, d, e]
    if xs.count(6) == 2: 
        count += 1

print(count / n, 5 * 4 / 2 * 5**3 / 6**5)