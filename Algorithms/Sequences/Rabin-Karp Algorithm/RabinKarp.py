#!/usr/bin/python


def rabin_karp(pattern, text):
    hpattern = hash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        hs = hash(text[i: i + len(pattern)])
        if hs == hpattern:
            if pattern == text[i: i + len(pattern)]:
                return i
    return -1


# TEST CASES
print(rabin_karp('pan', 'anpanman'))  # 2
print(rabin_karp('odetofood', 'ilikefoodfrommexico'))  # -1
print(rabin_karp('ABCDABD', 'ABCABCDABABCDABCDABDE'))  # 13
print(rabin_karp('caga', 'gcagagag'))  # 1
print(rabin_karp('abacaba', 'abaxyabacabbaababacaba'))  # 15
