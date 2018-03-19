#!/usr/bin/python

limit = 1000000
result = 0
phi = [i for i in range(0, limit + 1)]
for i in range(2, limit + 1):
    if phi[i] == i:
        for j in range(i, limit + 1, i):
            phi[j] = phi[j] // i * (i - 1)
    result += phi[i]
print(result)
