def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """

    # enumerate the 3**N possible combinations
    for i in range(3 ** len(items)):
        bag1 = []
        bag2 = []
        for j in range(len(items)):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            if (i // 3**j) % 3 == 2:
                bag2.append(items[j])

        yield (bag1, bag2)

test = yieldAllCombos(['a', 'b'])

