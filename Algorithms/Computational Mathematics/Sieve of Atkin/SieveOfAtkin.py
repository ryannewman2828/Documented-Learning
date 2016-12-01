#!/usr/bin/python
from datetime import datetime

# TODO make more efficient

limit = int(input("Enter the limit for the primes you want to find: "))
start = datetime.now()
arr = [True] * (limit + 61)

if limit >= 2:
    print(2)
if limit >= 3:
    print(3)
if limit >= 5:
    print(5)
if limit < 5:
    exit()

list1 = [1, 13, 17, 29, 37, 41, 49, 53]
list2 = [7, 19, 31, 43]
list3 = [11, 23, 47, 59]
x = 1
y = 1

w = 0
while w <= limit / 60:
    for x in list1 + list2 + list3:
        arr[60 * w + x] = False
    w += 1

x = 1
y = 1
n = 5
while n <= limit:
    while n <= limit:
        if n % 60 in list1:
            arr[n] = not arr[n]
        y += 2
        n = 4 * x * x + y * y
    x += 1
    y = 1
    n = 4 * x * x + y * y

x = 1
y = 2
n = 7
while n <= limit:
    while n <= limit:
        if n % 60 in list2:
            arr[n] = not arr[n]
        y += 2
        n = 3 * x * x + y * y
    x += 2
    y = 2
    n = 3 * x * x + y * y

x = 2
y = x - 1
n = 11
while n <= limit:
    while n <= limit and y >= 1:
        if n % 60 in list3:
            arr[n] = not arr[n]
        y -= 2
        n = 3 * x * x - y * y
    x += 1
    y = x - 1
    n = 3 * x * x - y * y

# TODO optimize this
w = 0
n = 0
while n * n <= limit:
    for x in list1 + list2 + list3:
        n = 60 * w + x
        if n * n > limit:
            break
        if arr[n]:
            c = 0
            q = 0
            while c <= limit:
                for y in list1 + list2 + list3:
                    c = n * n * (60 * w + y)
                    if c <= limit:
                        arr[c] = False
                q += 1
    w += 1
    n = w * w

n = 7
w = 0
primes = [2, 3, 5]
while n <= limit:
    for x in list1 + list2 + list3:
        n = 60 * w + x
        if n <= limit and arr[n]:
            print(n)
    w += 1

print("Time: " + (datetime.now() - start).__str__())
