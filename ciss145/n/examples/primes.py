import math
primes = []

for n in range(2, 100001):

    isprime = True
    for i in range(2, math.sqrt(n) + 1):
        if isprime and n % i == 0:
            isprime = False
            break

    if isprime:
        primes.append(n)

print primes
