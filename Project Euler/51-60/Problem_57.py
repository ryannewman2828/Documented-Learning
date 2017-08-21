#!/usr/bin/python

total = 0
num = 7
den = 5
n1 = 3
d1 = 2
for i in range(999):
    n2 = n1
    d2 = d1
    n1 = num
    d1 = den

    num = 2 * n1 + n2
    den = 2 * d1 + d2

    if len(str(num)) > len(str(den)):
        total += 1
print(total)
