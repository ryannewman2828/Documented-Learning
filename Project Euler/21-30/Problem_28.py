#!/usr/bin/python

n = 1
count = 1
stop = 1001 * 1001
increment = 2

while n < stop:
    count += 4 * n + 10 * increment
    n += 4 * increment
    increment += 2

print(count)
