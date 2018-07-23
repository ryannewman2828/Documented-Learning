#!/usr/bin/python


def kadanes(A):
    B = [A[0]]
    msub = B[0]
    for i in range(1, len(A)):
        B.append(max(A[i], B[i - 1] + A[i]))
        msub = max(msub, B[i])
    return msub


# TEST CASES
print(kadanes([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(kadanes([2, 3, -1, -20, 5, 10]))  # 15
