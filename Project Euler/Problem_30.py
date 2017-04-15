#!/usr/bin/python

count = 0
for i in range(2, 1000000):
    n = i
    s = 0
    while n > 0:
        s += (n % 10) ** 5
        n //= 10
    if s == i:
        count += s

print(count)
