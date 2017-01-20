#!/usr/bin/python

arr = [line.rstrip('\n') for line in open('problem_67.in')]

for i in range(0, len(arr)):
    arr[i] = list(arr[i].split(" "))
    for j in range(0, len(arr[i])):
        arr[i][j] = int(arr[i][j])

holdSums = arr[len(arr) - 1]

for i in range(len(arr) - 2, -1, -1):
    sums = arr[i]
    for j in range(0, len(sums)):
        if holdSums[j] > holdSums[j + 1]:
            sums[j] += holdSums[j]
        else:
            sums[j] += holdSums[j + 1]
    holdSums = sums

print(holdSums[0])
