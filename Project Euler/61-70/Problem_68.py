#!/usr/bin/python
import itertools


answer = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

combos = list(itertools.permutations(nums, 9))

for combo in combos:
    ring = [[0, 0, 0] for x in range(5)]
    ring[0][0] = 10  # for ring of size 16, 10 must be on the outside
    ring[0][1] = combo[0]
    ring[4][2] = combo[0]
    ring[0][2] = combo[1]
    ring[1][1] = combo[1]
    ring_sum = sum(ring[0])
    numCopy = list(combo[2:])
    i = 1

    for num in combo[2:]:
        if i == 4:
            temp = ring_sum - ring[4][1] - ring[4][2]
            if temp in numCopy:
                ring[4][0] = temp
                j = 0
                minRing = ring[0][0]

                for r in range(1, len(ring)):
                    if ring[r][0] < minRing:
                        j = r
                        minRing = ring[r][0]
                text = ''
                for k in range(5):
                    ring[(j + k) % 5] = [str(x) for x in ring[(j + k) % 5]]
                    text += ''.join(ring[(j + k) % 5])
                text = int(text)
                if text > answer:
                    answer = text
            break
        if num not in numCopy:
            continue
        ring[i][0] = num
        numCopy.remove(num)
        temp = ring_sum - ring[i][0] - ring[i][1]
        if temp in numCopy:
            numCopy.remove(temp)
            ring[i][2] = temp
            ring[(i + 1) % 5][1] = temp
        else:
            break
        i += 1

print(answer)
