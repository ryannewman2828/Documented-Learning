#!/usr/bin/python

arr = [line.rstrip('\n') for line in open('problem_11.in')]
max = 0

for i in range(0, len(arr)):
    arr[i] = arr[i].split()

for i in range(0, 20):
    for j in range(0, 20):
        arr[i][j] = int(arr[i][j])

for i in range(0, 16):
    for j in range(0, 16):
        num = arr[i][j] * arr[i][j + 1] * arr[i][j + 2] * arr[i][j + 3]
        if num > max:
            max = num
        num = arr[i][j] * arr[i + 1][j] * arr[i + 2][j] * arr[i + 3][j]
        if num > max:
            max = num
        num = arr[i][j] * arr[i + 1][j + 1] * arr[i + 2][j + 2] * arr[i + 3][j + 3]
        if num > max:
            max = num

for i in range(16, 20):
    for j in range(0, 16):
        num = arr[i][j] * arr[i][j + 1] * arr[i][j + 2] * arr[i][j + 3]
        if num > max:
            max = num
        num = arr[j][i] * arr[j + 1][i] * arr[j + 2][i] * arr[j + 3][i]
        if num > max:
            max = num

for i in range(3, 19):
    for j in range(0, 16):
        num = arr[i][j] * arr[i - 1][j + 1] * arr[i - 2][j + 2] * arr[i - 3][j + 3]
        if num > max:
            max = num

print(max)
