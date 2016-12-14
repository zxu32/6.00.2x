# From codereview.stackexchange.com
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        # total number of partitions of an n-element set is the Bell Number
        # total number of subsets of an n-element set is 2**n
        # this for loop iterate 'number of subset of an (len(set_)-1) element set' of times
        parts = [set(), set()]
        for item in set_:
            parts[i & 1].add(item)
            # 'i & 1' outputs '0, 1, 0, 1, 0, 1....'
            i >>= 1
            # 'i & 1' and 'i >> 1' lines produce /n
            # [(powerSet of first n-1 elements + last element), (reciprocal of powerSet of first n-1 element)]
        for b in partitions(parts[1]):
            # recursively calls partitions function to break down parts[1]
            # contains more than 1 element from previous step
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):  # partitions(set_) yields subsets one by one
        yield [list(elt) for elt in partition]  # converts subsets to lists

# Uncomment the following code  and run this file
# to see what get_partitions does if you want to visualize it:

if __name__ == '__main__':
    for item in (get_partitions({'a': 1, 'b': 2, 'c': 3, 'd': 4})):
        print(item)
