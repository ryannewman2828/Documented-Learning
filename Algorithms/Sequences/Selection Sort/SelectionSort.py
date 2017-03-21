#!/usr/bin/python
import random

maxNum = 1000000
# The array that is to be sorted
arr = [int(maxNum * random.random()) for i in range(10000)]

for i in range(len(arr)):
    index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[index]:
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp
print(arr)
