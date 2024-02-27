def merge__two__sort(left, right, firstIndex):
    i = j = 0
    s = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            s.append(left[i])
            i += 1
        else:
            s.append(right[j])
            j += 1
    s.extend(left[i:])
    s.extend(right[j:])
    print(str(firstIndex + 1) + ' ' + str(firstIndex + len(s)) + ' ' + str(s[0]) + ' ' + str(s[-1]))
    return s
def merge(arr, l, r):
    if (r - l == 1):
        return [arr[l]]
    middle = int((l + r) // 2)
    left = merge(arr, l, middle)
    right = merge(arr, middle, r)
    return merge__two__sort(left, right, l)
n = int(input())
arr = list(map(int, input().split()))
arr__sorted = merge(arr, 0, n)
for num in arr__sorted:
    print(num, end=' ')
