#!/usr/bin/python
import itertools
import math

n = 10000
prime = [True] * (n + 1)
count = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i]:
        j = i * i
        while j <= n:
            prime[j] = False
            j += i


for x in range(1488, 10000):
    digits = [int(x) for x in str(x)]
    n_digits = len(digits)
    n_power = n_digits - 1
    permutations = itertools.permutations(digits)
    arr = [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = arr[j] - arr[i]
            if diff == 0:
                break
            for k in range(j + 1, len(arr)):
                if arr[k] - arr[j] == diff:
                    if prime[arr[i]] and prime[arr[j]] and prime[arr[k]]:
                        print(str(arr[i]) + str(arr[j]) + str(arr[k]))
                        exit()
                elif arr[k] - arr[j] > diff:
                    break