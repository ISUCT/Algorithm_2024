def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merged = merge(left, right)

    return merged, inv_left + inv_right + inv_merged


def merge(left, right):
    merged = []
    i = j = inv = 0
    left_len = len(left)
    right_len = len(right)

    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += left_len - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv


n = int(input())
arr = list(map(int, input().split()))

_, inv = merge_sort(arr)
print(inv)
