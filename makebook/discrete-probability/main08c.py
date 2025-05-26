# file: main08c.py
import random; random.seed()
n = 1000000
count = 0
for _ in range(n):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    if [a, b].count(6) >= 1:
        count += 1
print(count / n, 11 / 36)