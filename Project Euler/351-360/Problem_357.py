#!/usr/bin/python
import math

n = 100000000
count = 3

isPrime = [True] * (n + 1)

k = int(math.sqrt(n))
for i in range(2, k + 1):
    if isPrime[i]:
        j = i * i
        while j <= n:
            isPrime[j] = False
            j += i


def valid(num):
    sq = int(math.sqrt(num))
    for d in range(1, sq + 1):
        if num % d == 0:
            if not isPrime[d + num // d]:
                return False
    return True


for i in range(6, n, 4):
    if not isPrime[1 + i]:
        continue

    if not isPrime[2 + i // 2]:
        continue

    if valid(i):
        count += i

print count
