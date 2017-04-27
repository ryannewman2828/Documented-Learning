#!/usr/bin/python

arr = [line.rstrip('\n') for line in open('problem_13.in')]

for i in range(0, len(arr)):
    arr[i] = list(arr[i])
    for j in range(0, len(arr[i])):
        arr[i][j] = int(arr[i][j])

count = 0
sum = 0
for i in range(49, 9, -1):
    sum = count
    for j in range(0, 100):
        sum += arr[j][i]
    count = sum / 10

sum = 0
arr = [line.rstrip('\n') for line in open('problem_13.in')]
for i in range(0, 100):
    sum += int(arr[i][:10])

sum += count
ans = str(sum)
print(ans[:10])
