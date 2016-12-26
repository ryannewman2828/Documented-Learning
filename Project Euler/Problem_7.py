#!/usr/bin/python
import math

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
        count += 1
        if count == 10001:
            print(i)
            break
