#!/usr/bin/python


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("greatest common divisor: " + str(gcd(a, b)))
