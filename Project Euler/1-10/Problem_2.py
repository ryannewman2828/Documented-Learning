#!/usr/bin/python

fib = 2
prev = 1
sum = 0

while fib < 4000000:
    if fib % 2 == 0:
        sum += fib
    fib += prev
    prev = fib - prev

print(sum)
