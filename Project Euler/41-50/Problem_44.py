#!/usr/bin/python

def isPenta(num):
    # is the inverse function an integer or not
    return ((24 * num + 1) ** 0.5 + 1) / 6 == int(((24 * num + 1) ** 0.5 + 1) / 6)

i = 1
while True:
    i += 1
    n = i * (3 * i - 1) // 2
    j = i - 1
    while j > 0:
        m = j * (3 * j - 1) // 2
        if isPenta(n - m) and isPenta(n + m):
            print(n - m)
            exit(0)
        j -= 1
