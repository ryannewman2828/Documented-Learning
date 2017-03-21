#!/usr/bin/python
import random

maxNum = 1000000
# The array that is to be sorted
arr = [int(maxNum * random.random()) for i in range(10000)]

for i in range(1, len(arr)):
    x = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > x:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = x
print(arr)
