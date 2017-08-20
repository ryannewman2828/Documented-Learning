#!/usr/bin/python
import math

total = 0
for n in range(1, 101):
    for r in range(n):
        if math.factorial(n) // math.factorial(r) // math.factorial(n - r) > 1000000:
            total += 1
print(total)
