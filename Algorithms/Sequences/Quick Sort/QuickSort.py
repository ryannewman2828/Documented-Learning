#!/usr/bin/python
import random

maxNum = 1000000
# The array that is to be sorted
array = [int(maxNum * random.random()) for i in range(100000)]


def partition(lo, hi):
    pivot = array[lo]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        temp = array[i]
        array[i] = array[j]
        array[j] = temp


def quickSort(lo, hi):
    if lo < hi:
        p = partition(lo, hi)
        quickSort(lo, p)
        quickSort(p + 1, hi)


quickSort(0, len(array) - 1)
print(array)
