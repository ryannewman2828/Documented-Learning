#!/usr/bin/python

sum = 0
count = 0
for i in range(1, 101):
    sum += i * i
    count += i

print(count * count - sum)