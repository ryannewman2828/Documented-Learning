#!/usr/bin/python
import math

total = 0
for i in range(1, 30):
    for j in range(1, 100):
        n = j ** i
        if len(str(n)) == i:
            total += 1
print(total)
