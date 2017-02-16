#!/usr/bin/python

# The array that is to be sorted
arr = [4, 65, 25, 12, 22, 11]

for i in range(1, len(arr)):
    x = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > x:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = x
print(arr)
