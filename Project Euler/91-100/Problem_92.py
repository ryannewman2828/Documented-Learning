#!/usr/bin/python

dyn = [0] * 10000001
dyn[89] = 89
dyn[1] = 1
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def chain(num):
    if dyn[num] == 89 or dyn[num] == 1:
        return dyn[num]
    else:
        temp = num
        n = num
        num = 0
        while n > 0:
            num += squares[n % 10]
            n //= 10
        dyn[temp] = chain(num)
        return dyn[temp]

total = 0
for i in range(2, 10000000):
    if chain(i) == 89:
        total += 1
print(total)
