#!/usr/bin/python


# Splits the number in half and returns as a tuple
def split(num, s):
    base = 10 ** s
    return num % base, num // base


def karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b
    m = max(len(str(a)), len(str(b)))
    m2 = m / 2
    aTuple = split(a, m2)
    bTuple = split(b, m2)
    aHigh = aTuple[1]
    aLow = aTuple[0]
    bHigh = bTuple[1]
    bLow = bTuple[0]
    pLow = karatsuba(aLow, bLow)
    pMid = karatsuba(aLow + aHigh, bLow + bHigh)
    pHigh = karatsuba(aHigh, bHigh)
    return (pHigh * 10 ** (2 * m2)) + ((pMid - pHigh - pLow) * 10 ** m2) + pLow


assert karatsuba(134351264321060546523, 9843957283619613876396246916) == \
       1322548106976807924913755284818715428557013273068
