#!/usr/bin/python

def palindrone(num):
    num = str(num)
    l = len(num)
    for i in range(l // 2):
        if num[i] != num[l - i - 1]:
            return False
    return True

total = 0
for i in range(10000):
    temp = i
    for j in range(50):
        temp += int(str(temp)[::-1])
        if palindrone(temp):
            total += 1
            break
print(10000 - total)
