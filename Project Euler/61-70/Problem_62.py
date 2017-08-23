#!/usr/bin/python
import math


def perm(a, b):
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        return False
    d = [0] * 10
    for x in a:
        d[int(x)] += 1
    for x in b:
        d[int(x)] -= 1
    for e in d:
        if e != 0:
            return False
    return True

n = 50
found = []
while True:
    x = n ** 3
    entry = True
    for f in found:
        if perm(f[0], x):
            f[1] += 1
            if x < f[0]:
                f[0] = x
            entry = False
            if f[1] == 5:
                print(f[0])
                exit()
    if entry:
        found.append([x, 1])
    n += 1
