#!/usr/bin/python
import math

arr = []
ans = {}
for i in range(1000):
    arr.append(i ** 2)

for i in range(1, 1000):
    for j in range(i, 1000):
        k = math.sqrt(arr[i] + arr[j])
        if int(k) == k:
            p = k + math.sqrt(arr[i]) + math.sqrt(arr[j])
            if p in ans:
                ans[p] += 1
            else:
                ans[p] = 0

largest = 0
index = 0
for i in range(1, 1000):
    if i in ans and ans[i] > largest:
        largest = ans[i]
        index = i

print(index)
