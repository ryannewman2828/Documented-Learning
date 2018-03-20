#!/usr/bin/python

factDict = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def calculate(n):
    total = 0
    while n > 0:
        total += factDict[n % 10]
        n = n // 10
    return total


numDict = {78: 4, 69: 5, 540: 2, 145: 1, 169: 3, 363601: 3, 1454: 3, 871: 2, 872: 2, 45361: 2, 45362: 2}
result = 0


def recurse(n, links):
    if n in links:
        return 0
    if n in numDict:
        return numDict[n]
    links.append(n)
    numDict[n] = 1 + recurse(calculate(n), links)
    return numDict[n]

limit = 1000000
for i in range(3, limit):
    if recurse(i, []) == 60:
        result += 1
print(result)
