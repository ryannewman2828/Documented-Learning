#!/usr/bin/python
from datetime import datetime
import math

n = int(input("Enter the limit for the primes you want to find: "))
start = datetime.now()
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

print("Time: " + (datetime.now() - start).__str__())
