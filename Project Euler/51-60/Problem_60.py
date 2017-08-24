#!/usr/bin/python
import math
import random

dict = {}

def isPrime(n, k):
    r = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        cont = False
        for __ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                cont = True
                break
        if cont:
            continue
        return False
    return True

def property(a, b):
    if (a, b) in dict:
        return dict[(a, b)]
    num = int(str(a) + str(b))
    if num < len(prime) and not prime[num]:
        dict[(a, b)] = False
        dict[(b, a)] = False
        return False
    elif not isPrime(num, 10):
        dict[(a, b)] = False
        dict[(b, a)] = False
        return False
    num = int(str(b) + str(a))
    if num < len(prime) and not prime[num]:
        dict[(a, b)] = False
        dict[(b, a)] = False
        return False
    elif not isPrime(num, 10):
        dict[(a, b)] = False
        dict[(b, a)] = False
        return False
    dict[(a, b)] = True
    dict[(b, a)] = True
    return True



n = 10000
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

for a in range(len(primes)):
    for b in range(len(primes)):
        if not property(primes[a], primes[b]):
            continue
        for c in range(len(primes)):
            if not (property(primes[a], primes[c]) and property(primes[b], primes[c])):
                continue
            for d in range(len(primes)):
                if not (property(primes[a], primes[d]) and property(primes[b], primes[d]) and property(primes[c], primes[d])):
                    continue
                for e in range(len(primes)):
                    if property(primes[a], primes[e]) and property(primes[b], primes[e]) and \
                            property(primes[c], primes[e]) and property(primes[d], primes[e]):
                        print(sum([primes[a], primes[b], primes[c], primes[d], primes[e]]))
                        exit()
