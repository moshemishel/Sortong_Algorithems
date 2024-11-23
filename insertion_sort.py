def insertion_sort(arr):
    comparisons_count = 0
    initializations_count = 0

    for i in range(1, len(arr)):
        num = arr[i]
        j = i -1
        while j >= 0 and num < arr[j]:
            comparisons_count += 1
            arr[j+1] = arr[j]
            initializations_count +=1
            j-=1
            
        if j != -1:
            comparisons_count+=1
        arr[j+1] = num
        initializations_count+=1
         


    return comparisons_count, initializations_count

