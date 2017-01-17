#!/usr/bin/python

singleDigits = [3, 3, 5, 4, 4, 3, 5, 5, 4]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
doubleDigits = [6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
wordAnd = 3

count = 10 * (sum(singleDigits) + sum(teens))  # counts to 19 for all appearances of it
count += wordAnd * 99 * 9  # counts the 'and' words
count += hundred * 900  # counts the "hundred" words
count += sum(doubleDigits) * 100  # counts all the double digit words minus the teens
count += sum(singleDigits) * 8 * 10  # counts all single appearances not including leading numbers
count += sum(singleDigits) * 100  # counts all leading numbers ie 'one' hundred and

print(count + 3 + 8)  # includes one thousand
