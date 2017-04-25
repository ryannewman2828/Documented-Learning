#!/usr/bin/python
import math

def isMagic(n):
    sum = 0
    for j in n:
        sum += math.factorial(int(j))
        if sum > int(n):
            return False
    return sum == int(n)

ans = 0
for i in range(3, 1000000):
    if isMagic(str(i)):
        ans += i

print(ans)
