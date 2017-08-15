#!/usr/bin/python
import itertools


def tupToInt(num):
    n = 0
    for i in num:
        n *= 10
        n += i
    return n

def isPrime(num):
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return False
    return True

nums = [1]
pans = [1]
for i in range(2, 10):
    nums.append(i)
    pans.extend(list(itertools.permutations(nums)))
for i in range(1, len(pans)):
    pans[i] = tupToInt(pans[i])

pans.sort()
for i in range(len(pans) - 1, -1, -1):
    if isPrime(pans[i]):
        print(pans[i])
        break
