#!/usr/bin/python
from datetime import datetime
import math

n = 2000000
sum = 0
arr = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = i * i
        while j <= n:
            arr[j] = False
            j += i

for i in range(2, n + 1):
    if arr[i]:
        sum += i

print(sum)