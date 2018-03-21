#!/usr/bin/python

dynamic = [0] * 101
dynamic[0] = 1
for i in range(1, 100):
    for j in range(i, 101):
        dynamic[j] += dynamic[j - i]
print(dynamic[100])
