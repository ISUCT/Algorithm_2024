def merge_list(left, right):
    result = []
    i = j = 0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return result, inv_count


def merge(array):
    if len(array) <= 1:
        return array, 0
    middle = len(array) // 2
    left, inv_left = merge(array[:middle])
    right, inv_right = merge(array[middle:])
    merged, count = merge_list(left, right)
    count += (inv_left + inv_right)
    return merged, count

n = int(input())
arr = list(map(int, input().split()))
merged__arr, counter = merge(arr)
print(counter)

