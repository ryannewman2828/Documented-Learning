#!/usr/bin/python

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

s = 0
sPrev = 1
t = 1
tPrev = 0
r = b
rPrev = a

while r != 0:
    q = rPrev // r
    tmp = r
    r *= -q
    r += rPrev
    rPrev = tmp
    tmp = s
    s *= -q
    s += sPrev
    sPrev = tmp
    tmp = t
    t *= -q
    t += tPrev
    tPrev = tmp
print("Bézout coefficients: " + str(sPrev) + ", " + str(tPrev))
print("greatest common divisor: " + str(rPrev))
print("quotients by the gcd: " + str(s) + ", " + str(t))
