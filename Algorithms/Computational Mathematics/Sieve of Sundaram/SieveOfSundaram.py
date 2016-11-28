#!/usr/bin/python

n = int(input("Enter the limit for the primes you want to find: "))
limit = int((n + 1) / 2)
arr = [True] * limit

m = len(arr)
for i in range(1, m):
    for j in range(i, m):
        if i + j + 2 * i * j < m:
            arr[i + j + 2 * i * j] = False

print(2)
for i in range(1, limit):
    if arr[i]:
        print(2 * i + 1)