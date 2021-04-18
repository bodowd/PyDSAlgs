"""
Binary search : search ordered list with divide and coquer strategy in logarithmic time O(log n)
"""

def binarySearch(alist, item):
    first = 0  # mark the starting index
    last = len(
        alist) - 1  # mark the last index, -1 because python starts with 0, the length is one longer than the last index
    found = False

    while first <= last and not found:
        # i.e. len(alist) = 5 then, (0 + 4)//2 = 2 index 2 is the first midpoint
        midpoint = (first + last) // 2
        if item == alist[midpoint]:
            found = True
        # shift the first (left window) to midpoint
        # don't include midpoint, we know that's not the number we want, so we shift one to the right.
        else:
            if item > alist[midpoint]:
                first = midpoint + 1
            # otherwise shift the right window (last) to midpoint
            else:
                last = midpoint - 1
    return found


alist = [1, 4, 6, 7, 9, 10, 15, 20, 22, 25, 60, 90, 300]
# alist = [1,2,20]
print(binarySearch(alist, 20))
print(binarySearch(alist, 3))


def recursiveBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if item == alist[midpoint]:
            return True
        else:
            if item > alist[midpoint]:
                # midpoint + 1 because python includes the first item for the slice
                return recursiveBinarySearch(alist[midpoint + 1:], item)
            else:
                # python goes up to but not including the last item for the slice
                return recursiveBinarySearch(alist[:midpoint], item)

print(recursiveBinarySearch(alist,20))
print(recursiveBinarySearch(alist,10))
