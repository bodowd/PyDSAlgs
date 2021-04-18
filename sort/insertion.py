"""
O(n^2) but shift operation uses ~1/3 less processing work as an exchange. So it will perform better than bubble and selection
sorts.
"""
#### first implementation
# def insertionSort(alist):
#     # [17, 2, 3]
#     for index in range(1,len(alist)): # insertion sort starts with the first item as an already sorted list
#         # index = 1 -> 2
#
#         currentvalue = alist[index]
#         # 2
#         position = index # two counters
#         # 1
#
#         # if the item to the left is larger, move it to the right
#         # go backwards again
#         while position>0 and alist[position-1]>currentvalue:
#             # 1 -> true, 17 -> true
#             alist[position] = alist[position-1]
#             # change index 1 to value at index 0, NOT a swap. Shifts the position
#             position = position - 1
#             # 1 - 1 = 0 -> position 0
#             # move position back one index. If we hit the beginning, index = 0 leave while loop, and go to nex
#
#         # when position-1 is < current value, we insert the current value here
#         alist[position] = currentvalue
#         # position = 0, currentvalue is 2. Since above was not a swap, we just made room behind the value that was moved up
#         # we now re-assign the index where the value was moved up from


def insertionSort(alist):
    for i in range(1,len(alist)):
        cur_val = alist[i]
        position = i

        # keep looking left at position-1 until the while loop breaks. Either you get to 0 or the position to the left
        # is smaller than the current value
        while position > 0 and alist[position-1] > cur_val:
            # if the position is not at the beginning of the list and the number to the left is larger than current value
            # assign the current position (which is toward the right side of the list) the larger value which is in
            # position -1
            alist[position] = alist[position-1]
            # then move back to position-1 (to the left)
            position = position-1
        # insert the cur val at the position
        # if the above while loop doesn't enter, then it just keeps the current position as cur_val, goes to next pass
        alist[position] = cur_val


# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist = [17,22,3]
insertionSort(alist)
print(alist)