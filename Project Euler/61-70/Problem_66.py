#!/usr/bin/python

max = 0
ans = 0
for D in range(2, 1001):
    n = int(D ** 0.5)
    if n ** 2 == D:
        continue
    d = 1
    m = 0
    a = n

    num = a
    den = 1
    n1 = 1
    d1 = 0

    while num ** 2 - D * den ** 2 != 1:
        m = d * a - m
        d = (D - m ** 2) // d
        a = (n + m) // d

        n2 = n1
        d2 = d1
        n1 = num
        d1 = den

        num = a * n1 + n2
        den = a * d1 + d2

    if num > max:
        max = num
        ans = D
print(ans)
