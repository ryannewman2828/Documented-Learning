#!/usr/bin/python

arr = [line.rstrip('\n') for line in open('Problem_89.in')]

def romanToInt(roman):
    total = 0
    r = 0
    while r < len(roman):
        if roman[r] == 'M':
            total += 1000
        elif roman[r] == 'D':
            total += 500
        elif roman[r] == 'C':
            if r + 1 < len(roman) and roman[r + 1] == 'D':
                total += 400
                r += 1
            elif r + 1 < len(roman) and roman[r + 1] == 'M':
                total += 900
                r += 1
            else:
                total += 100
        elif roman[r] == 'L':
            total += 50
        elif roman[r] == 'X':
            if r + 1 < len(roman) and roman[r + 1] == 'L':
                total += 40
                r += 1
            elif r + 1 < len(roman) and roman[r + 1] == 'C':
                total += 90
                r += 1
            else:
                total += 10
        elif roman[r] == 'V':
            total += 5
        elif roman[r] == 'I':
            if r + 1 < len(roman) and roman[r + 1] == 'X':
                total += 9
                r += 1
            elif r + 1 < len(roman) and roman[r + 1] == 'V':
                total += 4
                r += 1
            else:
                total += 1
        r += 1
    return total

def intToRoman(num):
    roman = ''
    while num > 0:
        if num >= 1000:
            roman += 'M'
            num -= 1000
        elif num // 100 == 9:
            roman += 'CM'
            num -= 900
        elif num >= 500:
            roman += 'D'
            num -= 500
        elif num // 100 == 4:
            roman += 'CD'
            num -= 400
        elif num >= 100:
            roman += 'C'
            num -= 100
        elif num // 10 == 9:
            roman += 'XC'
            num -= 90
        elif num >= 50:
            roman += 'L'
            num -= 50
        elif num // 10 == 4:
            roman += 'XL'
            num -= 40
        elif num >= 10:
            roman += 'X'
            num -= 10
        elif num == 9:
            roman += 'IX'
            num -= 9
        elif num >= 5:
            roman += 'V'
            num -= 5
        elif num == 4:
            roman += 'IV'
            num -= 4
        elif num >= 1:
            roman += 'I'
            num -= 1
    return roman

ans = 0
for i in arr:
    ans += len(i) - len(intToRoman(romanToInt(i)))
print(ans)
