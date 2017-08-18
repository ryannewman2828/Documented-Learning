#!/usr/bin/python
import math

n = 1000000
prime = [True] * (n + 1)
primes = []

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i]:
        j = i * i
        while j <= n:
            prime[j] = False
            j += i
for i in range(2, len(prime)):
    if prime[i]:
        primes.append(i)

size = 0
total = 0
ans = total
for i in range(len(primes)):
    total = 0
    for j in range(i, len(primes)):
        total += primes[j]
        if total >= 1000000:
            break
        if j - i > size and total in primes:
            size = j - i
            ans = total
print(ans)
