#!/usr/bin/python
import random

maxNum = 100000
# The array that is to be sorted
arr = [int(maxNum * random.random()) for i in range(100000)]

count = [0] * (maxNum + 1)
for i in range(len(arr)):
    count[arr[i]+1] += 1

for i in range(1, maxNum+1):
    count[i] += count[i-1]

arrB = arr.copy()
for i in range(len(arr)):
    arr[count[arrB[i]]] = arrB[i]
    count[arrB[i]] += 1

print(arr)
