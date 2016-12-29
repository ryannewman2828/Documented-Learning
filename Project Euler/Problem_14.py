#!/usr/bin/python

dict = {'1': 1}


def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        n = int(n / 2)
        if n in dict:
            dict[str(2 * n)] = dict[str(n)] + 1
            return dict[str(2 * n)]
        dict[str(2 * n)] = collatz(n) + 1
        return dict[str(2 * n)]
    else:
        n = 3 * n + 1
        if n in dict:
            dict[str(int((n - 1)/3))] = dict[str(n)] + 1
            return dict[str(int((n - 1)/3))]
        dict[str(int((n - 1) / 3))] = collatz(n) + 1
        return dict[str(int((n - 1)/3))]

max = 0
for i in range(1, 1000000):
    print(i)
    m = collatz(i)
    if m > max:
        max = m

print(max)
