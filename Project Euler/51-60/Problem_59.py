#!/usr/bin/python

arr = [line.rstrip('\n').split(',') for line in open('problem_59.in')][0]
arr = [int(x) for x in arr]
key = [65, 65, 65]

for i in range(len(arr) // 3 + 1):
    for j in range(3):
        if 3 * i + j < len(arr):
            while not (32 <= arr[3 * i + j] ^ key[j] <= 90 or 97 <= arr[3 * i + j] ^ key[j] <= 122):
                key[j] += 1

for i in range(len(arr) // 3 + 1):
    for j in range(3):
        if 3 * i + j < len(arr):
            arr[3 * i + j] ^= key[j]
print(sum(arr))
