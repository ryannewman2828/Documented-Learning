#!/usr/bin/python
import random

maxNum = 1000000
# The array that is to be sorted
arr = [int(maxNum * random.random()) for i in range(100000)]


def partition(array, lo, hi):
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


def quickSort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quickSort(array, lo, p)
        quickSort(array, p + 1, hi)


quickSort(arr, 0, len(arr) - 1)
print(arr)
