#!/usr/bin/python
import random

maxNum = 1000000
# The array that is to be sorted
arr = [int(maxNum * random.random()) for i in range(10000)]


def merge(listA, listB):
    listReturn = []
    while len(listA) > 0 or len(listB) > 0:
        if len(listA) == 0:
            listReturn.extend(listB)
            listB.clear()
        elif len(listB) == 0:
            listReturn.extend(listA)
            listA.clear()
        elif listA[0] < listB[0]:
            listReturn.append(listA.pop(0))
        else:
            listReturn.append(listB.pop(0))
    return listReturn


def mergeSort(array):
    if len(array) == 1:
        return array

    listA = mergeSort(array[:len(array) // 2])
    listB = mergeSort(array[len(array) // 2:])

    return merge(listA, listB)

print(mergeSort(arr))
