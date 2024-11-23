def counting_sort(arr, res_array, min_, max_):
    initializations_count = 0

    count = [0 for _ in range(max_ - min_ + 1)]
    initializations_count += max_ - min_ + 1
    for num in arr:
        count[num-min_] += 1
        initializations_count += 1

    for i in range(1, len(count)):
        count[i] += count[i-1-min_]
        initializations_count += 1

    for j in range(len(arr)-1, -1, -1):
        initializations_count += 1
        res_array[count[ar r[j]-min_]-1] = arr[j]
        count[arr[j]-min_] -= 1

    return comparisons_count:=0, initializations_count


