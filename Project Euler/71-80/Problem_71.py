#!/usr/bin/python

a = 3
b = 7
r = 0
s = 1
limit = 1000000

for q in range(limit, 2, -1):
    p = (a * q - 1) // b
    if p * s > r * q:
        s = q
        r = p
print r, '/', s
