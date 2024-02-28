def merge(A: list, L: list, R: list) -> list:
    i, j, k = 0, 0, 0
    while k < len(A):
        if (j == len(R) or (i < len(L) and L[i] <= R[j])):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    return A


def merge_sort(arr: list, start=1):
    if len(arr) <= 1:
        return arr, start
    L, R = arr[:len(arr) // 2], arr[len(arr) // 2:]
    L, _ = merge_sort(L, start)
    R, _ = merge_sort(R, start + len(arr) // 2)
    res = merge(arr, L, R)
    print(start, start + len(arr) - 1, res[0], res[-1])
    return res, start


N = int(input())
A = list(map(int, input().split()))
res, _ = merge_sort(A)
print(*res)
