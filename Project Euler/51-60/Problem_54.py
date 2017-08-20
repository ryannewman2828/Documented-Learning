#!/usr/bin/python

arr = [line.rstrip('\n').split(' ') for line in open('problem_54.in')]
hands = []

def generate(hand):
    flush = True
    suit = hand[0][1]
    present = []
    for i in range(len(hand)):
        if hand[i][1] != suit:
            flush = False
        if hand[i][0] == 'T':
            present.append(10)
        elif hand[i][0] == 'J':
            present.append(11)
        elif hand[i][0] == 'Q':
            present.append(12)
        elif hand[i][0] == 'K':
            present.append(13)
        elif hand[i][0] == 'A':
            present.append(14)
        else:
            present.append(int(hand[i][0]))
    present.sort()
    present.reverse()
    vals = []
    freq = []
    for i in present:
        if i in vals:
            freq[vals.index(i)] += 1
        else:
            vals.append(i)
            freq.append(1)
    return [vals, freq, flush]

def straight(hand):
    for i in range(1, len(hand)):
        if hand[i - 1] - 1 % 13 != hand[i] % 13:
            return False
    return len(hand) == 5


def nOfAKind(hand, n):
    for i in range(len(hand[1])):
        if hand[1][i] == n:
            return hand[0][i]
    return 0  # no quads

# can hand1 beat hand2 with a full house
def fullHouse(hand1, hand2):
    return nOfAKind(hand1, 2) != 0 and nOfAKind(hand1, 3) > nOfAKind(hand2, 3) or \
           (nOfAKind(hand1, 3) != 0 and nOfAKind(hand1, 3) == nOfAKind(hand2, 3) and nOfAKind(hand1, 2) > nOfAKind(hand2, 2))

def twoPair(hand1, hand2):
    count = 0
    for i in range(len(hand1[1])):
        if hand1[1][i] == 2:
            count += 1
    if count != 2:
        return False
    count = 0
    for i in range(len(hand2[1])):
        if hand2[1][i] == 2:
            count += 1
    if count != 2:
        return True
    index1 = 0
    index2 = 0
    for i in range(len(hand1[1])):
        if hand1[1][i] == 2:
            index1 = i
            break
    for i in range(len(hand2[1])):
        if hand2[1][i] == 2:
            index2 = i
            break
    if hand1[0][index1] > hand2[0][index2]:
        return True
    for i in range(len(hand1[1]) - 1, -1, -1):
        if hand1[1][i] == 2:
            index1 = i
            break
    for i in range(len(hand2[1]) - 1, -1, -1):
        if hand2[1][i] == 2:
            index2 = i
            break
    return hand1[0][index1] > hand2[0][index2]

for hand in arr:
    hands.append([generate(hand[:5]), generate(hand[5:])])

total = 0
for hand in hands:
    if hand[0][0] == [14, 13, 12, 11, 10] and hand[0][2]:
        total += 1
    elif hand[1][0] == [14, 13, 12, 11, 10] and hand[1][2]:
        continue
    elif straight(hand[0][0]) and hand[0][2] and \
            (not straight(hand[1][0] or not hand[1][2] or hand[0][0][0] > hand[1][0][0])):
        total += 1
    elif straight(hand[1][0]) and hand[1][2] and \
            (not straight(hand[0][0] or not hand[0][2] or hand[1][0][0] > hand[0][0][0])):
        continue
    elif nOfAKind(hand[0], 4) > nOfAKind(hand[1], 4):
        total += 1
    elif nOfAKind(hand[0], 4) < nOfAKind(hand[1], 4):
        continue
    elif fullHouse(hand[0], hand[1]):
        total += 1
    elif fullHouse(hand[1], hand[0]):
        continue
    elif hand[0][2] and (not hand[1][2] or hand[0][0][0] > hand[1][0][0]):
        total += 1
    elif hand[1][2] and (not hand[0][2] or hand[1][0][0] > hand[0][0][0]):
        continue
    elif straight(hand[0][0]) and (not straight(hand[1][0]) or hand[0][0][0] > hand[1][0][0]):
        total += 1
    elif straight(hand[1][0]) and (not straight(hand[0][0]) or hand[1][0][0] > hand[0][0][0]):
        continue
    elif nOfAKind(hand[0], 3) > nOfAKind(hand[1], 3):
        total += 1
    elif nOfAKind(hand[0], 3) < nOfAKind(hand[1], 3):
        continue
    elif twoPair(hand[0], hand[1]):
        total += 1
    elif twoPair(hand[1], hand[0]):
        continue
    elif nOfAKind(hand[0], 2) > nOfAKind(hand[1], 2):
        total += 1
    elif nOfAKind(hand[0], 2) < nOfAKind(hand[1], 2):
        continue
    elif hand[0][0][0] > hand[1][0][0]:
        total += 1

print(total)
