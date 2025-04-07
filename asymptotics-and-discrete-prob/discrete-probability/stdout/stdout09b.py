# file: main09b.py
import random; random.seed()
n = 1000000
count = 0
for _ in range(n):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    c = random.randrange(1, 7)
    d = random.randrange(1, 7)
    e = random.randrange(1, 7)
    xs = [a,b,c,d,e]
    if xs.count(6) >= 2: 
        count += 1

print(count / n, 1 - 2 * 5**5/6**5)