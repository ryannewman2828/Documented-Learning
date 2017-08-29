#!/usr/bin/python

ans = 1

for _ in range(7830457):
    ans *= 2
    ans %= 10000000000

ans *= 28433
ans %= 10000000000
ans += 1
print(ans)
