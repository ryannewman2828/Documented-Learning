#!/usr/bin/python

denoms = [200, 100, 50, 20, 10, 5, 2, 1]


def branch(total, index):
    if total < 0:
        return 0
    elif total == 0:
        return 1
    else:
        count = 0
        for j in range(index, len(denoms)):
            count += branch(total - denoms[j], j)
        return count

print(branch(200, 0))
