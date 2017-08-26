#!/usr/bin/python

arr = [list(line.rstrip('\n')) for line in open('problem_79.in')]
chars = ['0', '1', '2', '3', '6', '7', '8', '9']
ans = ""

while len(arr) > 0:
    char = arr[0][0]
    for i in range(len(arr)):
        if arr[i][1] == char:
            char = arr[i][0]
    ans += char
    chars.remove(char)
    for i in range(len(arr)):
        if char in arr[i]:
            arr[i].remove(char)
        if len(arr[i]) == 0 or len(arr[i]) == 1:
            arr[i] = []
    while [] in arr:
        arr.remove([])
ans += str(chars[0])
print(ans)
