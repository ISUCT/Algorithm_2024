def merge_two_list(a, b):
    c = []
    i = j = 0
    inv_count = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inv_count += len(a) - i
    c += a[i:]
    c += b[j:]
    return c, inv_count

def merge_sort(s):
    if len(s) <= 1:
        return s, 0
    middle = len(s) // 2
    left, left_inversions = merge_sort(s[:middle])
    right, right_inversions = merge_sort(s[middle:])
    merged_list, inversions = merge_two_list(left, right)
    return merged_list, left_inversions + right_inversions + inversions

n = int(input())
result, inv_count = merge_sort(list(map(int, input().split())))
print(inv_count)