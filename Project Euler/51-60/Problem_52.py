#!/usr/bin/python

def same(x, y):
    x = str(x)
    y = str(y)
    if len(x) != len(y):
        return False
    for j in x:
        if j not in y:
            return False
    return True

i = 1
while True:
    n = 2 * i
    if same(n, 3 * i) and same(n, 4 * i) and same(n, 5 * i) and same(n, 6 * i):
        print(i)
        break
    i += 1