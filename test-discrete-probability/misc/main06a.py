# file: main06a.py
import random; random.seed()
n = 1000000
count = 0
for _ in range(n):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    if a == 6 and b == 6:
        count += 1
print(count / n, 1 / 36)