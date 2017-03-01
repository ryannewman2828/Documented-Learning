#!/usr/bin/python


def fact(n):
    f = 1
    for p in range(2, n + 1):
        f *= p
    return f

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 0

count = 0
for i in range(9, 0, -1):
    k = fact(i)
    j = 0
    while True:
        if count + k >= 1000000:
            ans += pow(10, i) * numbers[j]
            numbers.remove(numbers[j])
            break
        j += 1
        count += k
print(ans)
