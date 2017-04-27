#!/usr/bin/python

ans = ""
i = 1

while len(ans) <= 1000000:
    ans += str(i)
    i += 1

print(int(ans[0]) * int(ans[9]) * int(ans[99]) * int(ans[999]) *
      int(ans[9999]) * int(ans[99999]) * int(ans[999999]))
