#!/usr/bin/python
from datetime import datetime

n = int(input("Enter the limit for the primes you want to find: "))
start = datetime.now()
if n <= 1:
    exit()

limit = (n + 1) // 2
arr = [True] * limit

m = len(arr)
i = 1
incr = 3
x = 4
while x < m:
    while x < m:
        arr[x] = False
        x += incr
    i += 1
    incr += 2
    x = (incr + 1) * i

print(2)
for i in range(1, limit):
    if arr[i]:
        print(2 * i + 1)

print("Time: " + (datetime.now() - start).__str__())
