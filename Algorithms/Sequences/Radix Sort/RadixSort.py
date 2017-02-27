#!/usr/bin/python
import random
import math
from queue import Queue

maxNum = 1000
# The array that is to be sorted
arr = [int(maxNum * random.random()) for i in range(0, 10000)]
digit = 1

# Because the max in our list is 1000
iters = math.log10(maxNum)
while digit <= iters:
    buckets = [Queue() for i in range(0, 10)]
    for i in range(0, len(arr)):
        index = 0
        if arr[i] < 10 ** iters:
            index = int((arr[i] % (10 ** digit)) / (10 ** (digit - 1)))
        buckets[index].put(arr[i])
    arr = []
    digit += 1
    for i in range(0, 10):
        while not buckets[i].empty():
            arr.append(buckets[i].get())
print(arr)
