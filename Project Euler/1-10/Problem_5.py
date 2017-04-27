#!/usr/bin/python

i = 2520
while True:
    loop = True
    for j in range(11, 21):
        if i % j != 0:
            loop = False
    if loop:
        print(i)
        break
    i += 2520
