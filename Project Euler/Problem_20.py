#!/usr/bin/python


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def sumNum(n):
    return sum([int(i) for i in str(n)])

print(sumNum(fact(100)))
