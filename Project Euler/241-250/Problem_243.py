#!/usr/bin/python
# http://www.geeksforgeeks.org/eulers-totient-function/
# This one took a lot of trial and error as well as research into the nature of this problem
import math

def phi(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result *= 1.0 - (1.0 / i)
        i += 1
    if n > 1:
        result *= 1.0 - (1.0 / i)
    return int(result)

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

denom = 94744
num = 15499

# loop through the primes and multiply until the property is met
d = 6  # 2 * 3
for p in range(2, len(primes)):
    count = phi(d)
    if count * denom < num * (d - 1):
        break
    d *= primes[p]

# loop through the composite numbers and multiply until property is met
k = 4
prev = 4
while True:
    if not prime[k]:
        temp = d * k
        count = phi(temp)
        if count * denom < num * (temp - 1):
            print(temp)
            exit()
        prev = k
    k += 1
