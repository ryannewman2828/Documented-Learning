#!/usr/bin/python
import math

n = 10000
arr = [True] * (n + 1)
primes = []
limit = 1000000

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = i * i
        while j <= n:
            arr[j] = False
            j += i

for i in range(2, len(arr)):
    if arr[i]:
        primes.append(i)

temp = 1
k = 0
while temp * primes[k] < limit:
    temp *= primes[k]
    k += 1

print(temp)
