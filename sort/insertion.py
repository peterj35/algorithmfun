def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = currentvalue
        print(alist)


alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

# [26, 54, 93, 17, 77, 31, 44, 55, 20]
# [26, 54, 93, 17, 77, 31, 44, 55, 20]
# [17, 26, 54, 93, 77, 31, 44, 55, 20]
# [17, 26, 54, 77, 93, 31, 44, 55, 20]
# [17, 26, 31, 54, 77, 93, 44, 55, 20]
# [17, 26, 31, 44, 54, 77, 93, 55, 20]
# [17, 26, 31, 44, 54, 55, 77, 93, 20]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]