#!/usr/bin/python

fib = {}


def recurse(n):
    if n < 3:
        return 1
    elif n in fib:
        return fib[n]
    else:
        fib[n] = recurse(n - 1) + recurse(n - 2)
        return fib[n]

a = 1
while True:
    b = str(recurse(a))
    if len(b) == 1000:
        print(a)
        break
    a += 1
