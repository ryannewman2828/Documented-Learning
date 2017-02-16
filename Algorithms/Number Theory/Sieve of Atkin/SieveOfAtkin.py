#!/usr/bin/python
from datetime import datetime

limit = int(input("Enter the limit for the primes you want to find: "))
start = datetime.now()
arr = [True] * (limit + 61)

if limit < 5:
    exit()
if limit >= 2:
    print(2)
if limit >= 3:
    print(3)
if limit >= 5:
    print(5)

list1 = [1, 13, 17, 29, 37, 41, 49, 53]
list2 = [7, 19, 31, 43]
list3 = [11, 23, 47, 59]
listW = list1 + list2 + list3

for x in listW:
    for w in range(int(limit / 60) + 1):
        arr[60 * w + x] = False


x = 4
y = 0
n = 5
N = 5
while n <= limit:
    while n <= limit:
        if n % 60 in list1:
            arr[n] = not arr[n]
        y += 8
        n += y
    x += 8
    N += x
    y = 0
    n = N

x = 0
y = 4
n = 7
N = 7
while n <= limit:
    while n <= limit:
        if n % 60 in list2:
            arr[n] = not arr[n]
        y += 8
        n += y
    x += 24
    N += x
    y = 4
    n = N

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

for x in listW:
    n = x
    while n * n <= limit:
        if arr[n]:
            for y in listW:
                c = n * n * y
                while c <= limit:
                    arr[c] = False
                    c += n * n * 60
        n += 60

for x in listW:
    n = x
    while n < limit:
        if arr[n]:
            print(n)
        n += 60

print("Time: " + (datetime.now() - start).__str__())
