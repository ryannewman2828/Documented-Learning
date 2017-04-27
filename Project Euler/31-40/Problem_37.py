#!/usr/bin/python
import math

nums = 1000000
arr = [True] * (nums + 1)
arr[1] = False

for i in range(2, int(math.sqrt(nums)) + 1):
    if arr[i]:
        j = i * i
        while j <= nums:
            arr[j] = False
            j += i


def leftPrime(n):
    while n > 10:
        if not arr[n]:
            return False
        n = int(str(n)[1:])
    return arr[n]


def rightPrime(n):
    while n > 0:
        if not arr[n]:
            return False
        n //= 10
    return True

i = 10
ans = 0
count = 11
while count > 0:
    if leftPrime(i) and rightPrime(i):
        ans += i
        count -= 1
    i += 1

print(ans)
