def selectionSort(alist):
    # count backwards -- marks the right side edge of the list
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        # start counting from the left side edge of the list and count towards the right side edge
        for location in range(1, fillslot+1):
            # find the largest position
            if alist[location]>alist[positionOfMax]:
                positionOfMax=location
        # swap the largest position. Only one swap per iteration
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp



alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
