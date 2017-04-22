#!/usr/bin/python
import fractions

den = 1
nom = 1

for i in range(1, 10):
    for j in range(1, i):
        for k in range(1, j):
            if (k * 10 + i) * j == k * (i * 10 + j):
                den *= j
                nom *= k
print(den / fractions.gcd(nom, den))
