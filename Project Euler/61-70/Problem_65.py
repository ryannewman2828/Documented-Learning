#!/usr/bin/python

num = 11
numP = 8
denom = 4
denomP = 3
k = 4

for i in range(5, 101):
    temp1 = num
    temp2 = denom
    if i % 3 == 0:
        num = num * k + numP
        denom = denom * k + denomP
        k += 2
    else:
        num += numP
        denom += denomP
    numP = temp1
    denomP = temp2
num = str(num)
total = 0
for s in num:
    total += int(s)
print(total)
