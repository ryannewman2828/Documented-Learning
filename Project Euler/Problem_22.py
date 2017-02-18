#!/usr/bin/python

arr = [line[1:-1] for line in open('problem_22.in').read().split(",")]
arr.sort()
ans = 0
for i in range(0, len(arr)):
    name = arr[i]
    count = 0
    for j in name:
        count += ord(j) - 64
    ans += count * (i + 1)
print(ans)
