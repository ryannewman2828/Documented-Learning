#!/usr/bin/python

def isPal(n):
    n = str(n)
    for l in range(0, int(len(n)/2)):
        if n[l] != n[len(n) - l - 1]:
            return False
    return True

max = 0
k = 0

for i in range(900, 1000):
    for j in range(900, 1000):
        k = i * j
        if k > max and isPal(k):
            max = k

print(max)
