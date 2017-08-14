#!/usr/bin/python

triNums = [1, 3]

def isTri(num):
    if num in triNums:
        return True
    elif num > triNums[len(triNums) - 1]:
        while num > triNums[len(triNums) - 1]:
            triNums.append((len(triNums) * (len(triNums) + 1)) // 2)
        return num == triNums[len(triNums) - 1]

def wordToNum(word):
    total = 0
    for i in word:
        total += ord(i) - 64
    return total

arr = [line[1:-1] for line in open('problem_42.in').read().split(",")]
count = 0
for word in arr:
    if isTri(wordToNum(word)):
        count += 1
print(count)
