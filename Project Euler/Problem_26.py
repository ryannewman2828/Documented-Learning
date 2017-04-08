#!/usr/bin/python


def divide(n):
    curNum = 10
    history = [10]
    while curNum > 0:
        temp = curNum // n
        curNum -= n * temp
        curNum *= 10
        if curNum in history:
            return len(history)
        history.append(curNum)
    return 0


index = 0
maxNum = 0
for i in range(1, 1000):
    num = divide(i)
    if num > maxNum:
        maxNum = num
        index = i

print(index)
