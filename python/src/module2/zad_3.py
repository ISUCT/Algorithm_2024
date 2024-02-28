def merge_sort(arr, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    k = start
    i = j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if start + i < mid:
        while k < end:
            arr[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            arr[k] = right[j]
            j += 1
            k += 1
    print(f"{start + 1} {end} {arr[start]} {arr[end - 1]}")


n = int(input())

arr = list(map(int, input().split()))

merge_sort(arr, 0, n)

print(' '.join(map(str, arr)))
