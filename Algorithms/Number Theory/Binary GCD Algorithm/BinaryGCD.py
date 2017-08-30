#!/usr/bin/python


def gcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    if a % 2 == 0:
        if b % 2 == 1:
            return gcd(a // 2, b)
        else:
            return 2 * gcd(a // 2, b // 2)

    if b % 2 == 0:
        return gcd(a, b // 2)

    if a > b:
        return gcd((a - b) // 2, b)

    return gcd((b - a) // 2, a)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("greatest common divisor: " + str(gcd(a, b)))
