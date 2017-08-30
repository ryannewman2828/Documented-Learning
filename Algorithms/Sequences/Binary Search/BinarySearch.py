#!/usr/bin/python


def binarySearch(array, target):
    left = 0
    right = len(array)
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Sentinel because target is not in the array


# The array that is to be searched
arr = [0, 5, 7, 13, 14, 16, 19, 22, 32, 37, 41, 45, 55, 68, 72, 79, 81, 87, 98]

print(binarySearch(arr, 16))
