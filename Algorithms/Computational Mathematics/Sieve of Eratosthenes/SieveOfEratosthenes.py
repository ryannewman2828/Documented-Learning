#!/usr/bin/python
import math

n = int(input("Enter the limit for the primes you want to find: "))
arr = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = i * i
        while j <= n:
            arr[j] = False
            j += i

for i in range(2, n + 1):
    if arr[i]:
        print(i)
