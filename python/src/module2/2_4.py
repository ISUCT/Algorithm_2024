def merge(A, L, R):
    inv = 0
    i, j, k = 0, 0, 0
    while k < len(A):
        if j == len(R) or (i < len(L) and L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inv += len(L) - i
        k += 1
    return inv


def count_inv(arr: list):
    if len(arr) <= 1:
        return 0
    L, R = arr[:len(arr) // 2], arr[len(arr) // 2:]
    L_inv = count_inv(L)
    R_inv = count_inv(R)
    inv = merge(arr, L, R)
    return inv + L_inv + R_inv


N = int(input())
A = list(map(int, input().split()))
res = count_inv(A)
print(res)
