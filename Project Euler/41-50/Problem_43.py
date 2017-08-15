#!/usr/bin/python
import itertools

primes = [2, 3, 5, 7, 11, 13, 17]
def tupToInt(num):
    n = 0
    for i in num:
        n *= 10
        n += i
    return n

def property(num):
    num = str(num)
    for i in range(7):
        if int(num[i+1:i+4]) % primes[i] != 0:
            return False
    return True

pans = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
for i in range(len(pans)):
    pans[i] = tupToInt(pans[i])

total = 0
for i in pans:
    if property(i):
        total += i
print(total)
