#!/usr/bin/python

arr = [[1],[1],[1],[1],[1],[1]]

def cyclical(orig, num):
    return orig % 100 == num // 100

def generate(chain, indexes):
    if len(indexes) == 0 and cyclical(chain[5], chain[0]):
        print(sum(chain))
        exit()
    n = chain[len(chain) - 1]
    for i in indexes:
        for j in arr[i]:
            if j not in chain and cyclical(n, j):
                temp1 = chain.copy()
                temp1.append(j)
                temp2 = indexes.copy()
                temp2.remove(i)
                generate(temp1, temp2)

n = 1
while arr[0][len(arr[0]) - 1] < 10000:
    n += 1
    f = n * (n + 1) // 2
    if f > 1000:
        arr[0].append(f)

n = 1
while arr[1][len(arr[1]) - 1] < 10000:
    n += 1
    f = n * n
    if f > 1000:
        arr[1].append(f)

n = 1
while arr[2][len(arr[2]) - 1] < 10000:
    n += 1
    f = n * (3 * n - 1) // 2
    if f > 1000:
        arr[2].append(f)

n = 1
while arr[3][len(arr[3]) - 1] < 10000:
    n += 1
    f = n * (2 * n - 1)
    if f > 1000:
        arr[3].append(f)

n = 1
while arr[4][len(arr[4]) - 1] < 10000:
    n += 1
    f = n * (5 * n - 3) // 2
    if f > 1000:
        arr[4].append(f)

n = 1
while arr[5][len(arr[5]) - 1] < 10000:
    n += 1
    f = n * (3 * n - 2)
    if f > 1000:
        arr[5].append(f)

for n in arr[0]:
    generate([n], [1, 2, 3, 4, 5])
