#!/usr/bin/python
import random


# The array that is to be sorted
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def partition(left, right, index):
    pivot = array[index]
    temp = array[index]
    array[index] = array[right]
    array[right] = temp
    saveIndex = left
    for i in range(left, right):
        if array[i] < pivot:
            temp = array[saveIndex]
            array[saveIndex] = array[i]
            array[i] = temp
            saveIndex += 1
        temp = array[right]
        array[right] = array[saveIndex]
        array[saveIndex] = temp
        return saveIndex


def quickSelect(left, right, k):
    if left == right:
        return array[right]
    pivot = left + int(random.random() % (right - left + 1))
    pivot = partition(left, right, pivot)
    if k == pivot:
        return array[k]
    elif k < pivot:
        return quickSelect(left, pivot - 1, k)
    else:
        return quickSelect(pivot + 1, right, k)

print(quickSelect(0, len(array) - 1, 5))
