#!/usr/bin/python


def numDivisors(n):
    count = 0
    j = 1
    max = n
    while j < max:
        if n % j == 0:
            count += 2
            max = n / j
        j += 1
    return count

i = 2
num = 1
while numDivisors(num) <= 500:
    num += i
    i += 1
print(num)
