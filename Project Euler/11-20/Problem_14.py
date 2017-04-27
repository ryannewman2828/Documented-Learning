#!/usr/bin/python

r = 100000000
dict = [0] * r
dict[1] = 1

def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        k = int(n/2)
        if n < r and dict[k] != 0:
            dict[n] = dict[k] + 1
            return dict[n]
        if n < r:
            dict[n] = collatz(k) + 1
            return dict[n]
        else:
            return collatz(k) + 1
    else:
        k = 3 * n + 1
        if k < r and dict[k] != 0:
            dict[n] = dict[k] + 1
            return dict[n]
        if n < r:
            dict[n] = collatz(k) + 1
            return dict[n]
        else:
            return collatz(k) + 1

max = 0
index = 0
for i in range(1, 1000000):
    m = collatz(i)
    if m > max:
        max = m
        index = i

print(index)
