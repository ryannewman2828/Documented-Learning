#!/usr/bin/python
import math

n = 1000000
prime = [True] * (n + 1)
primes = []

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i]:
        j = i * i
        while j <= n:
            prime[j] = False
            j += i
for i in range(2, len(prime)):
    if prime[i]:
        primes.append(i)

dict = {}
for i in range(len(primes) - 1, -1, -1):
    temp = str(primes[i])
    for j in range(len(temp)):
        for k in range(j + 1, len(temp)):
            for x in range(k + 1, len(temp)):
                if temp[j] == temp[k] and temp[k] == temp[x]:
                    copy = list(temp)
                    copy[j] = '*'
                    copy[k] = '*'
                    copy[x] = '*'
                    copy = ''.join(copy)
                    if copy in dict:
                        dict[copy] += 1
                        if dict[copy] == 8:
                            print(primes[i])
                            exit()
                    else:
                        dict[copy] = 1
