#!/usr/bin/python

total = 0
founds = [False] * 12001
factors = {}
for i in range(2, 24001):
    stack = []
    found = False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            val = j + i // j
            stack.append((2, val))  # tuple of length of factor list and sum of list
            if j in factors:
                for f in factors[j]:
                    stack.append((f[0] + 1, f[1] + val - j))
            if i // j in factors:
                for f in factors[i // j]:
                    stack.append((f[0] + 1, f[1] + val - i // j))
    stack = list(set(stack))
    if len(stack) > 0:
        factors[i] = stack.copy()
    for s in stack:
        k = s[0] + i - s[1]
        if 2 <= k <= 12000:
            if not founds[k]:
                if not found:
                    total += i
                    found = True
                founds[k] = True
print(total)
