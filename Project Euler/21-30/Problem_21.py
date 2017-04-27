#!/usr/bin/python


def divisors(n):
    count = 1
    for j in range(2, n):
        if n % j == 0:
            count += j
    return count

sum = 0
for i in range(2, 10000):
    k = divisors(i)
    if divisors(k) == i and not i == k:
        sum += i
print(sum)
