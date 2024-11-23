from random import randint
def randomized_partition(arr, start, end):
    comparisons_count = 0
    initializations_count = 0
    pivot_i =  randint(start, end)
    arr[end], arr[pivot_i] = arr[pivot_i], arr[end]
 
    initializations_count+=1
    pivot_val = arr[end]
    i, j  = start, start

    k = end-1
    while j <= k:
        comparisons_count+=1
        if arr[j] < pivot_val:
            arr[i], arr[j] = arr[j], arr[i]
            initializations_count+=1
            i+=1
            j+=1
        elif arr[j] > pivot_val:
            arr[j], arr[k] = arr[k], arr[j]
            initializations_count+=1
            k-=1
        else:
            j+=1

    arr[j], arr[end] = arr[end], arr[j]
    initializations_count+=1
    return i, j, comparisons_count, initializations_count

def _quick_sort(arr, start, end):
    if end <= start:
        return 0,0
    i, j, comparisons_count, initializations_count= randomized_partition(arr, start, end)
    l_comparisons_count, l_initializations_count = _quick_sort(arr, start, i-1)
    r_comparisons_count, r_initializations_count = _quick_sort(arr, j+1, end)
    sum_comparisons = comparisons_count + l_comparisons_count + r_comparisons_count
    sum_initializations = initializations_count +  l_initializations_count+r_initializations_count
    return sum_comparisons, sum_initializations

def quick_sort(arr):
    return _quick_sort(arr, 0, len(arr)-1)
