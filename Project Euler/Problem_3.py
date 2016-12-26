#!/usr/bin/python

def recurse(n):
    for i in range(2, n):
        if n % i == 0:
            return max(recurse(i), recurse(int(n / i)))
    return n

print(recurse(600851475143))
