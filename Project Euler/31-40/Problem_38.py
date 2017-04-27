#!/usr/bin/python


def pandigital(num):
    num = str(num)
    if len(num) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in num:
            return False
    return True

largest = 0
for i in range(1000, 10000):
    nums = []
    nums.extend([str(i * 1), str(i * 2)])
    i = int(''.join(nums))
    if i > largest and pandigital(i):
        largest = i

for i in range(100, 1000):
    nums = []
    nums.extend([str(i * 1), str(i * 2), str(i * 3)])
    i = int(''.join(nums))
    if i > largest and pandigital(i):
        largest = i

for i in range(10, 100):
    nums = []
    nums.extend([str(i * 1), str(i * 2), str(i * 3), str(i * 4)])
    i = int(''.join(nums))
    if i > largest and pandigital(i):
        largest = i

for i in range(1, 10):
    nums = []
    nums.extend([str(i * 1), str(i * 2), str(i * 3), str(i * 4), str(i * 5)])
    i = int(''.join(nums))
    if i > largest and pandigital(i):
        largest = i

print(largest)
