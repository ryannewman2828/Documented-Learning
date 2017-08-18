#!/usr/bin/python
import random


def isPrime(n, k):
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = a ** d % n
        if x == 1 or x == n - 1:
            continue
        cont = False
        for __ in range(r - 1):
            x = x ** 2 % n
            if x == 1:
                return False
            if x == n - 1:
                cont = True
                break
        if cont:
            continue
        return False
    return True
