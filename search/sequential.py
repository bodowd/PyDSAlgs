'''Sequential search'''


def sequentialSearch(alist, item):
    """
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    >> sequentialSearch(testlist, 3)
    False
    >> sequentialSearch(testlist, 13)
    True

    :param alist:
    :param item:
    :return:
    """
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist,3))
print(sequentialSearch(testlist,13))


