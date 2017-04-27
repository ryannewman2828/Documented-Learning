#!/usr/bin/python

ans = 0
for i in range(1000000):
    if str(i) == str(i)[::-1] and "{0:b}".format(i) == "{0:b}".format(i)[::-1]:
        ans += i

print(ans)
