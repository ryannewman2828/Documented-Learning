#!/usr/bin/python
import itertools

def contains(a, b, l1, l2):
    l1 = l1.copy()
    l2 = l2.copy()
    if 6 in l1:
        l1.append(9)
    if 9 in l1:
        l1.append(6)
    if 6 in l2:
        l2.append(9)
    if 9 in l2:
        l2.append(6)
    return (a in l1 and b in l2) or (a in l2 and b in l1)

dices = list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
for d in range(len(dices)):
    dices[d] = list(dices[d])
    dices[d].sort()

total = 0
for i in range(len(dices)):
    a = dices[i]
    for j in range(i + 1, len(dices)):
        b = dices[j]
        if a == b:
            continue
        if not contains(0, 1, a, b):
            continue
        if not contains(0, 4, a, b):
            continue
        if not contains(0, 9, a, b):
            continue
        if not contains(1, 6, a, b):
            continue
        if not contains(2, 5, a, b):
            continue
        if not contains(3, 6, a, b):
            continue
        if not contains(4, 9, a, b):
            continue
        if not contains(6, 4, a, b):
            continue
        if not contains(8, 1, a, b):
            continue
        total += 1

print(total)
