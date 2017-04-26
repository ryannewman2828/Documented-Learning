#!/usr/bin/python
import math

n = 1000000
count = 13
arr = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = i * i
        while j <= n:
            arr[j] = False
            j += i


def circular(num):
    if not arr[num]:
        return False
    for _ in range(len(str(num)) - 1):
        temp = num % 10
        num -= temp
        num //= 10
        temp *= 10 ** len(str(num))
        num += temp
        if not arr[num]:
            return False
    return True

for i in range(100, 1000000):
    if circular(i):
        count += 1

print(count)
