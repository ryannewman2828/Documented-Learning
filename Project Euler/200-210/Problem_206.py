#!/usr/bin/python


def check(num):
    num = str(num)
    if len(num) != 17:
        return False
    count = 1
    for i in range(0, 18, 2):
        if num[i] != str(count):
            return False
        count += 1
    return True

ans = 138902663  # sqrt(19293949596979899)
while not check(ans ** 2):
    ans -= 1
print ans * 10
