#!/usr/bin/python
import math

n = 10000
arr = [True] * (n + 1)
primes = []
limit = 10000000
best = 1
bestRatio = 10000000000000000000000000000000000000000000000000000  # large number


def perm(a, b):
    track = [0] * 10
    a = str(a)
    b = str(b)

    if len(a) != len(b):
        return False

    for k in a:
        track[int(k)] += 1

    for k in b:
        track[int(k)] -= 1

    for i in track:
        if i != 0:
            return False
    return True

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = i * i
        while j <= n:
            arr[j] = False
            j += i

for i in range(2, len(arr)):
    if arr[i] and 2000 < i < 5000:
        primes.append(i)

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        n = primes[i] * primes[j]

        if n > limit:
            break

        phi = (primes[i] - 1) * (primes[j] - 1)
        ratio = n / phi

        if perm(n, phi) and bestRatio > ratio:
            best = n
            bestRatio = ratio

print(best)
