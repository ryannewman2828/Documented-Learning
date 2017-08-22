#!/usr/bin/python

arr = [line.rstrip('\n') for line in open('Problem_81.in')]
arr = [x.split(',') for x in arr]
for i in arr:
    for j in range(len(i)):
        i[j] = int(i[j])

paths = [
    (4445, (0, 0))  # (sum, (row, col))
]

row = 2

while row <= len(arr):
    temp = paths.copy()
    paths = []
    for i in range(row - 1):
        m = 1000000000
        for k in range(len(temp)):
            if temp[k][0] < m and ((temp[k][1][0] == i and temp[k][1][1] == row - 2)
                                   or (temp[k][1][0] == i - 1 and temp[k][1][1] == row - 1)):
                m = temp[k][0]
        temp.append((arr[i][row - 1] + m, (i, row - 1)))
        paths.append((arr[i][row - 1] + m, (i, row - 1)))
    for j in range(row - 1):
        m = 1000000000
        for k in range(len(temp)):
            if temp[k][0] < m and ((temp[k][1][1] == j and temp[k][1][0] == row - 2)
                                   or (temp[k][1][1] == j - 1 and temp[k][1][0] == row - 1)):
                m = temp[k][0]
        temp.append((arr[row - 1][j] + m, (row - 1, j)))
        paths.append((arr[row - 1][j] + m, (row - 1, j)))
    m = 1000000000
    for k in range(len(temp)):
        if ((temp[k][1][0] == row - 1 and temp[k][1][1] == row - 2) or (temp[k][1][1] == row - 1 and temp[k][1][0] == row - 2)) and temp[k][0] < m:
            m = temp[k][0]
    paths.append((arr[row - 1][row - 1] + m, (row - 1, row - 1)))
    row += 1

ans = 0
for k in range(len(paths)):
    if paths[k][1][0] == paths[k][1][1] == len(arr) - 1:
        ans = paths[k][0]
print(ans)
