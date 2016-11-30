#!/usr/bin/python

# TODO make more efficient
# TODO make work

limit = int(input("Enter the limit for the primes you want to find: "))
arr = [False] * (limit + 1)
if limit <= 1:
    exit()
elif limit == 2:
    print(2)
    exit()
elif limit <= 4:
    print(2 + "\n" + 3)
    exit()

arr[2] = arr[3] = arr[5] = True
list1 = [1, 13, 17, 29, 37, 41, 49, 53]
list2 = [7, 19, 31, 43]
list3 = [11, 23, 47, 59]
x = 1
y = 1

while x * x < limit:
    while y * y < limit:
        n = 4 * x * x + y * y
        if n <= limit and n % 60 in list1:
            arr[n] = not arr[n]

        n = 3 * x * x + y * y
        if n <= limit and n % 60 in list2:
            arr[n] = not arr[n]

        n = 3 * x * x - y * y
        if n <= limit and n % 60 in list3:
            arr[n] = not arr[n]
        y += 1
    x += 1

x = 7
while x * x < limit:
    if arr[x]:
        y = x * x
        while y < limit:
            arr[y] = False
            y += x * x
    x += 1

for i in range(2, limit + 1):
    if arr[i]:
        print(i)