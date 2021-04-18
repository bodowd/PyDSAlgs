"""

O(n^2) like bubble sort but a little faster than bubble sort since there's only one exchange per round
"""
def selectionSort(alist):

    # like bubble sort, get the number of passes. After each pass, we know the last slot will have the right number
    # passnum will
    # selection sort moves backwards through the list, thus range(len(alist)-1,0,-1)
    for passnum in range(len(alist)-1, 0, -1):
        max_position = 0
        # get the index of the max number
        for i in range(1, passnum+1):
            if alist[i] > alist[max_position]:
                max_position = i
        # swap largest position. only one swap per iteration
        # passnum starts from furthest position to 0 not including 0. So passnum will be the last index at this round
        # we swap here with simultaneous assignment
        alist[passnum], alist[max_position] = alist[max_position], alist[passnum]




alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
