##################################################
###
###  CODE TO COMPUTE THE MODIFIED STANDARD SCORE
import heapq
import random


medianAndDeviation = []

def getMedian( alist ):
    """return median of alist"""
    if alist == []:
        return []
    blist = sorted(alist)
    length = len(alist)
    if length % 2 == 1:
        # length of list is odd so return middle element
        return blist[int(((length + 1) / 2) - 1)]
    else:
        # length of list is even so compute midpoint
        v1 = blist[int(length / 2)]
        v2 = blist[(int(length / 2) - 1)]
        return (v1 + v2) / 2.0


def getAbsoluteStandardDeviation( alist, median ):
    """given alist and median return absolute standard deviation"""
    sum = 0
    for item in alist:
        sum += abs(item - median)
    return sum / len(alist)


def normalizeColumn(columnNumber ):
    """given a column number, normalize that column in self.data"""
    # first extract values to list
    col = [v[1][columnNumber] for v in data]

    median = getMedian(col)
    asd = getAbsoluteStandardDeviation(col, median)
    # print("Median: %f   ASD = %f" % (median, asd))
    medianAndDeviation.append((median, asd))
    for v in data:
        v[1][columnNumber] = (v[1][columnNumber] - median) / asd


def normalizeVector(v ):
    """We have stored the median and asd for each column.
    We now use them to normalize vector v"""
    vector = list(v)
    for i in range(len(vector)):
        (median, asd) = medianAndDeviation[i]
        vector[i] = (vector[i] - median) / asd
    return vector


###
### END NORMALIZATION
##################################################
data = []
k=3


def manhattan(vector1, vector2 ):
    """Computes the Manhattan distance."""
    return sum(map(lambda v1, v2: abs(v1 - v2), vector1, vector2))


def nearestNeighbor( itemVector ):
    """return nearest neighbor to itemVector"""
    return min([(manhattan(itemVector, item[1]), item)
                for item in data])


def knn(itemVector ):
    """returns the predicted class of itemVector using k
    Nearest Neighbors"""
    # changed from min to heapq.nsmallest to get the
    # k closest neighbors
    neighbors = heapq.nsmallest(k,
                                [(manhattan(itemVector, item[1]), item)
                                 for item in data])
    # each neighbor gets a vote
    results = {}
    for neighbor in neighbors:
        theClass = neighbor[1][0]
        results.setdefault(theClass, 0)
        results[theClass] += 1
    resultList = sorted([(i[1], i[0]) for i in results.items()], reverse=True)
    # get all the classes that have the maximum votes
    maxVotes = resultList[0][0]
    possibleAnswers = [i[1] for i in resultList if i[0] == maxVotes]
    # randomly select one of the classes that received the max votes
    answer = random.choice(possibleAnswers)
    return (answer)


def classify( itemVector ):
    """Return class we think item Vector is in"""
    # k represents how many nearest neighbors to use
    return knn(normalizeVector(itemVector))

