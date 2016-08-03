def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

def orderedSeqSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos <= len(alist) and not stop and not found:
        if alist[pos] == item:
            found = True
        else:
            if item < alist[pos]:
                stop = True
            else:
                pos += 1

    return found


testlist = [1,3,6,8,20,14,15]
print(sequentialSearch(testlist, 0))
print(sequentialSearch(testlist, 14))

mylist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 69]
print(orderedSeqSearch(mylist, 8))
print(orderedSeqSearch(mylist, 32))