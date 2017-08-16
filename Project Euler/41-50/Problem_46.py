#!/usr/bin/python
import math
primes = []

def conjecture(num):
    i = 0
    while i < len(primes) and primes[i] < num:
        a = (num - primes[i]) // 2
        if a ** 0.5 == int(a ** 0.5):
            return True
        i += 1
    return False

n = 1000000
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
    elif not conjecture(i):
        print(i)
        break
