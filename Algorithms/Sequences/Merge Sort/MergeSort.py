#!/usr/bin/python

# The array that is to be sorted
arr = [65, 25, 12, 22, 11, 45, 23, 5, 56, 11, 89]


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

    listA = mergeSort(array[:int(len(array) / 2)])
    listB = mergeSort(array[int(len(array) / 2):])

    return merge(listA, listB)

print(mergeSort(arr))
