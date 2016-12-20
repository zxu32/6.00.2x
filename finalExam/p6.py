import numpy as np


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    results = []
    resultSums = []
    resXchoi = []
    powerSetLength = 2**len(choices)
    npChoices = np.array(choices)
    # these lists are for cases when there's no match for total
    resultsClosest = []
    resXchoiClosest = []

    for i in range(powerSetLength):
        result = np.append(np.zeros(len(choices) - len(bin(i)[2:]), dtype=np.int64),
                           list(bin(i)[2:]))
        result = result.astype(np.int64)
        rXc = sum(np.multiply(npChoices, result)) - total

        if rXc == 0:  # record results matching total
            results.append(result)
            resultSums.append(sum(result))
            resXchoi.append(rXc)

        if rXc <= 0:  # record results that doesn't go over total
            resultsClosest.append(result)
            resXchoiClosest.append(rXc)

    if resXchoi:
        return results[resultSums.index(min(resultSums))]
    else:
        return resultsClosest[resXchoiClosest.index(max(resXchoiClosest))]

print(find_combination(choices=[1,2,2,3], total=4))
print(find_combination(choices=[1,1,3,5,3], total=5))
print(find_combination(choices=[4, 6, 3, 5, 2], total=10))
print(find_combination([1, 3, 4, 2, 5], 16))
print(find_combination([1], 10))
print(find_combination([1, 81, 3, 102, 450, 10], 9))