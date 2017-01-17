#!/usr/bin/python

arr = [0] * 401
arr[400] = 2
index = 1
carry = 0
for i in range(1, 1000):
    for j in range(400, 400 - index - 1, -1):
        arr[j] *= 2
        arr[j] += carry
        carry = int(arr[j] / 10)
        if arr[j] >= 10:
            if j - 1 == 400 - index:
                index += 1
            arr[j] %= 10

print(sum(arr))
