def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    inversions = 0
    mid = len(arr) // 2
    left, inv_left = mergeSort(arr[:mid])
    right, inv_right = mergeSort(arr[mid:])

    inversions += inv_left + inv_right

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions
n = int(input())
arr = list(map(int, input().split()))
sorted_arr, inv_count = mergeSort(arr)
print(inv_count)