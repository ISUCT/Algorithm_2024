def merge_two_list(a, b, indexes_values):
    c = []
    i = j = 0
    while i <len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c += a[i:]
    if j<len(b):
        c += b[j:]
    start_idx = indexes_values[0]
    end_idx = indexes_values[1]
    print(start_idx, end_idx, c[0], c[-1])
    return c

def merge_sort(s, start=1):
    if len(s) <= 1:
        return s, start
    middle = len(s)//2
    left, left_indexes = merge_sort(s[:middle], start)
    right, right_indexes = merge_sort(s[middle:], start + middle)
    return merge_two_list(left, right, [start, start + len(s) - 1]), start

n = int(input())
result, _ = merge_sort(list(map(int, input().split())))
print(' '.join(map(str, result)))