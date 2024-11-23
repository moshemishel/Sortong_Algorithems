def merge(arr1, arr2):
    comparisons_count = 0
    initializations_count = 0
    i, j = 0, 0 
    lenArr1, lenArr2  = len(arr1), len(arr2)
    res = []

    while i < lenArr1 and j < lenArr2:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
        comparisons_count+=1
        initializations_count+=1
    if i < lenArr1:
        initializations_count+= lenArr1-i
    else:
        initializations_count+=lenArr2-j
    return res + arr1[i:] + arr2[j:], comparisons_count, initializations_count

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0, 0
    mid = len(arr)//2
    leftArr, l_comparisons_count, l_initializations_count = merge_sort(arr[:mid])
    rightArr, r_comparisons_count, r_initializations_count = merge_sort(arr[mid:])
    newArr, comparisons_count, initializations_count = merge(leftArr, rightArr)
    sum_comparison = l_comparisons_count+r_comparisons_count+comparisons_count
    sum_initializations = l_initializations_count+r_initializations_count+initializations_count
    return newArr, sum_comparison, sum_initializations

def performanceMergeSort(arr):
    newArr, sum_comparison, sum_initializations = merge_sort(arr)
    arr[:] = newArr
    return sum_comparison, sum_initializations
