# array to be sorted TODO REWRITE THIS HSIt
# l and r are indexes
# return a sorted array
def mergeSort(array, l, r):
    # divides array into two halves, calls itself for the two halves
    # then merges the two sorted halves
    if r > l:
        m = (l + (r-1)) // 2

        mergeSort(array, l, m)
        mergeSort(array, m+1, r)
        merge(array, l, m, r)

def merge(arr, l, m, r):
    # given arr, where l to m is sorted and m to r is sorted,
    # merge into arr

    # want to select first item of l to m array, and first item of m+1 to r array
    # assume that both halves are sorted

    n1 = m - l + 1
    n2 = r - m

    # temporary left and right arrays
    l1 = []
    l2 = []

    # store values into arrays
    for i in range(0, n1):
        l1.append(arr[l + i])

    for i in range(0, n2):
        l2.append(arr[m + 1 + i])

    # now compare and insert into arr
    i = 0 # index to iterate l1
    j = 0 # index to iterate l2
    k = l # initial index in subarr to be replaced

    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            arr[k] = l1[i]
            i+=1
        else:
            arr[k] = l2[j]
            j+=1
        k+=1

    while i < n1:
        arr[k] = n1[i]
        i+=1
        k+=1

    while j < n2:
        arr[k] = n2[i]
        j+=1
        k+=1


test_arr = [38,27,43,3,9,82,10]
print(mergeSort(test_arr, 0, len(test_arr)))