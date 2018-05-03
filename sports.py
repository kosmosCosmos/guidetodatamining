list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54, 76, 68,
         61, 58, 70, 70, 70, 63, 65, 66, 61]
list2 = [66, 162, 204, 90, 99, 106, 175, 123, 68,
         200, 163, 95, 77, 108, 155, 155, 108, 106, 97, 76]

list3 = [(74, 190), (64, 101), (57, 87), (60, 97), (70, 140), (64, 102)]

import numpy as np


def normalizeColumn( list1 ):
    sum1 = 0
    sum2 = 0
    normalize = []
    if len(list1) % 2 != 0:
        midnum = list1[int(len(list1) / 2)]
    else:
        midnum = (int((list1[int((len(list1)) / 2)][0] + list1[int((len(list1)) / 2) - 1][0]) / 2),
                  int((list1[int((len(list1)) / 2)][1] + list1[int((len(list1)) / 2) - 1][1]) / 2))

    for score in list1:
        sum1 = sum1 + abs(score[0] - midnum[0])
        sum2 = sum2 + abs(score[1] - midnum[1])
    base1 = int(sum1 / len(list1))
    base2 = int(sum2 / len(list1))
    for score in list1:
        normalize.append(((score[0] - midnum[0]) / base1, score[1] - midnum[1] / base2))
    return normalize, base1, base2, midnum


def scorenormal( score, midnum, base1, base2 ):
    return ((score[0] - midnum[0]) / base1, score[1] - midnum[1] / base2)


def manhattannumpy( vector1, vector2 ):
    return sum(np.abs(np.array(vector1) - np.array(vector2)))


a, b, c, d = normalizeColumn(list3)
distance=[]
for score in a:
    distance.append(manhattannumpy(score, scorenormal([60, 140], d, c, b)))
distance.sort(reverse=True)
print(distance)
