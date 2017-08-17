#!/usr/bin/python
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

total = 0
for N in range(2, 10001):
    n = int(N ** 0.5)
    if n ** 2 == N:
        continue
    odd = 0
    d = 1
    m = 0
    a = n
    while True:
        m = d * a - m
        d = (N - m ** 2) // d
        a = (n + m) // d
        odd = 1 - odd
        if a == 2 * n:
            break
    total += odd
print(total)
