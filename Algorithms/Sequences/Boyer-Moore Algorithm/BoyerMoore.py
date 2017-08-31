#!/usr/bin/python


def char_to_int(char):
    return ord(char.lower()) - 97


def last_occur(pattern):
    last = [-1] * 26
    for i in range(len(pattern)):
        last[char_to_int(pattern[i].lower())] = i
    return last


def good_suffix(pattern):
    suffix = [0] * len(pattern)
    indexes = [-1]
    last_char = pattern[len(pattern) - 1]
    j = 1
    for i in range(len(pattern) - 1):
        if pattern[i] == last_char:
            indexes.append(i)
    last = True
    for i in range(len(pattern) - 2, -1, -1):
        if last and pattern[i] != last_char:
            suffix[len(suffix) - 1] = i
            last = False

        x = 0
        for k in range(len(indexes)):
            k -= x
            if indexes[k] - j < 0:
                suffix[i] = indexes[k] - j
            elif pattern[indexes[k] - j] != pattern[i]:
                suffix[i] = indexes[k] - j
                indexes.remove(indexes[k])
                x += 1
        j += 1
    return suffix


def boyer_moore(pattern, text):
    L = last_occur(pattern)
    S = good_suffix(pattern)
    i = len(pattern) - 1
    j = i
    while i < len(text) and j >= 0:
        if text[i] == pattern[j]:
            i -= 1
            j -= 1
        else:
            i += len(pattern) - 1 - min(L[char_to_int(text[i])], S[j])
            j = len(pattern) - 1
    if j == -1:
        return i + 1
    else:
        return -1


# TEST CASES
print(boyer_moore('pan', 'anpanman'))  # 2
print(boyer_moore('odetofood', 'ilikefoodfrommexico'))  # -1
print(boyer_moore('ABCDABD', 'ABCABCDABABCDABCDABDE'))  # 13
print(boyer_moore('caga', 'gcagagag'))  # 1
print(boyer_moore('abacaba', 'abaxyabacabbaababacaba'))  # 15
