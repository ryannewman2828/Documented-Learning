#!/usr/bin/python

ans = 0
for i in range(1, 1001):
    temp = 1
    for j in range(i):
        temp *= i
        temp %= 10000000000
    ans += temp
    ans %= 10000000000
print(ans)
