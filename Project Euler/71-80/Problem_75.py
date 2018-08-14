#!/usr/bin/python
import math


def gcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    if a % 2 == 0:
        if b % 2 == 1:
            return gcd(a // 2, b)
        else:
            return 2 * gcd(a // 2, b // 2)

    if b % 2 == 0:
        return gcd(a, b // 2)

    if a > b:
        return gcd((a - b) // 2, b)

    return gcd((b - a) // 2, a)


n = 1500000
ans = 0
sqr = int(math.sqrt(n))
triangles = [0] * (n + 1)

for i in range(2, sqr):
    for j in range(1, i):
        if (i + j) % 2 == 1 and gcd(i, j) == 1:
            a = i * i + j * j
            b = i * i - j * j
            c = 2 * i * j
            p = a + b + c
            while p <= n:
                triangles[p] += 1
                p += a + b + c

for i in range(n + 1):
    if triangles[i] == 1:
        ans += 1
print(ans)
