"""

makes multiple passes through a list. compares adjacent items and exchanges those that are out of order. each pass through
    the list places the next largest value in its proper place. each item "bubbles" up to the location it belongs.

Most inefficient sorting algorithm. But could be modified to end early if it notices no exchanges are occurring,
 which means it's already a sorted list

O(n^2)
since each time it places the largest number in the back,
for the first pass, n-1 comparisons,
second pass, n-2 comparisons,
etc.
on pass n-1 there is 1 comparison

"""

def bubbleSort(alist):
    # range starts at the len(alist)-1, goes to 0 but not including 0, and it goes backward by -1
    # because each pass will put the largest number remaining in the back, we cycle down from the len(alist)-1 to zero
    # first pass goes all the way to the end of the list
    # second pass doesn't need to go all the way to the end because we now know the largest number is at the end of list
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                # # swap with a three step swap procedure
                # temp = alist[i]
                # alist[i]=alist[i+1]
                # alist[i+1]=temp
                # python allows you to do simultaneous assignment
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
tmp = alist.copy()
print('Original list: ', tmp)
bubbleSort(alist)
print('Sorted list: ', alist)
