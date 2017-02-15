#!/usr/bin/python

# The array that is to be sorted
arr = [65, 25, 12, 22, 11]

for i in range(0, len(arr)):
    index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[index]:
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp
print(arr)
