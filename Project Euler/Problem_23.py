#!/usr/bin/python


def divisors(n):
    count = 0
    for j in range(int(n / 2), 0, -1):
        if n % j == 0:
            count += j
            if count > n:
                return True
    return count > n

sum = 0
arr = []
for i in range(2, 28124):
    if divisors(i):
        arr.append(i)

d = {}
for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        d[arr[i] + arr[j]] = True

for i in range(0, 28124):
    if i not in d:
        sum += i
print(sum)
