#!/usr/bin/python


def pandigital(one, two, three):
    if len(one) + len(two) + len(three) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in one and str(i) not in two and str(i) not in three:
            return False
    return True

prev = []
count = 0
for i in range(0, 10):
    for j in range(1000, 10000):
        if pandigital(str(i), str(j), str(i * j)):
            if i * j not in prev:
                prev.append(i * j)
                count += i * j
for i in range(10, 100):
    for j in range(100, 1000):
        if pandigital(str(i), str(j), str(i * j)):
            if i * j not in prev:
                prev.append(i * j)
                count += i * j

print(count)
