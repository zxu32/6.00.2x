def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    sumVal = 0
    if not L:
        return sumVal
    for i in L:
        for j in L:
            sub = L[L.index(i):L.index(j)+1]
            if sum(sub) > sumVal:
                sumVal = sum(sub)
    return sumVal
