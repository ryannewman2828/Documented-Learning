#!/usr/bin/python
import math

numPrimes = 1000
arr = [True] * (numPrimes + 1)
primes = []
for i in range(2, int(math.sqrt(numPrimes)) + 1):
    if arr[i]:
        j = i * i
        while j <= numPrimes:
            arr[j] = False
            j += i

for i in range(2, numPrimes + 1):
    if arr[i]:
        primes.append(i)

maxNum = 0
product = 0
for a in range(-999, 1000, 2):
    for b in range(-999, 1000, 2):
        n = 0
        count = 0
        num = n ** 2 + a * n + b
        while num in primes:
            count += 1
            num = n ** 2 + a * n + b
            n += 1
        if maxNum < count:
            maxNum = count
            product = a * b

print(product)
