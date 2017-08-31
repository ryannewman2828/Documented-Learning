#!/usr/bin/python


def failure_array(pattern):
    f = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            f[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = f[j - 1]
        else:
            f[i] = 0
            i += 1
    return f


def KMP(pattern, text):
    F = failure_array(pattern)
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                return i - j
            else:
                i += 1
                j += 1
        else:
            if j > 0:
                j = F[j - 1]
            else:
                i += 1
    return -1


# TEST CASES
print(KMP('pan', 'anpanman'))  # 2
print(KMP('odetofood', 'ilikefoodfrommexico'))  # -1
print(KMP('ABCDABD', 'ABCABCDABABCDABCDABDE'))  # 13
print(KMP('caga', 'gcagagag'))  # 1
print(KMP('abacaba', 'abaxyabacabbaababacaba'))  # 15
