def mergeSort(arr, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid, end)
        merge(arr, start, mid, end)
    return arr


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    print(f"{start + 1} {end} {arr[start]} {arr[end - 1]}")


N = int(input())
arr = list(map(int, input().split()))

sorted_arr = mergeSort(arr, 0, N)

print(' '.join(map(str, sorted_arr)))
