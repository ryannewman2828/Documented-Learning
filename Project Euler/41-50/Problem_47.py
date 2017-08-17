#!/usr/bin/python
import math
primes = []

def factors(num):
    total = 0
    r = num
    for p in primes:
        if p ** 2 > num:
            return total + 1
        f = False
        while r % p == 0:
            f = True
            r //= p
        if f:
            total += 1
        if r == 1:
            return total
    return total

n = 100000
arr = [True] * (n + 1)
count = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = i * i
        while j <= n:
            arr[j] = False
            j += i

for i in range(2, n + 1):
    if arr[i]:
        primes.append(i)

i = 650
count = 0
while True:
    if factors(i) == 4:
        count += 1
    else:
        count = 0
    if count == 4:
        print(i - 3)
        break
    i += 1
