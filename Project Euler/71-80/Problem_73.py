#!/usr/bin/python

limit = 12000
a = 1
b = 3
c = 4000
d = 11999
result = 0

while not (c == 1 and d == 2):
    result += 1
    k = (limit + b) / d
    e = k * c - a
    f = k * d - b
    a = c
    b = d
    c = e
    d = f
print(result)
