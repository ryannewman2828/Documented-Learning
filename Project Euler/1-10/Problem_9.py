#!/usr/bin/python

c = 1
loop = True
while loop:
    cSq = c * c
    for a in range(1, 1000 - c):
        b = 1000 - a - c
        if a * a + b * b == cSq:
            print(a*b*c)
            loop = False
            break
    c += 1
