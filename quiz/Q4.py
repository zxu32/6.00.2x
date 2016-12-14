def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    sCopy = s
    listCopy = L[:]
    multiplierSum = 0

    if not listCopy:
        return 'no solution'

    while sCopy:
        for i in listCopy:
            if i <= sCopy:
                multiplierSum += sCopy // i
                sCopy = sCopy % i
                listCopy = listCopy[listCopy.index(i):]  # slice useless integers off from the list
                break

        if sCopy == 0:
            return multiplierSum

        if listCopy[-1] > sCopy:
            return 'no solution'
