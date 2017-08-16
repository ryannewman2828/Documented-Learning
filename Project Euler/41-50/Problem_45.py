#!/usr/bin/python

def isPenta(num):
    # is the inverse function an integer or not
    return ((24 * num + 1) ** 0.5 + 1) / 6 == int(((24 * num + 1) ** 0.5 + 1) / 6)

def isTri(num):
    return ((8 * num + 1) ** 0.5 - 1) / 2 == int(((8 * num + 1) ** 0.5 - 1) / 2)

i = 144
while True:
    i += 1
    n = i * (2 * i - 1)
    if isPenta(n) and isTri(n):
        print(n)
        break
