def partition(A: list, L: int, r: int) -> int:
    v = A[(L + r - 1)//2]
    i = L
    j = r - 1
    while i <= j:
        while (A[i] < v):
            i += 1
        while A[j] > v:
            j -= 1
        if (i >= j):
            break
        q = A[i]
        A[i] = A[j]
        A[j] = q
        i += 1
        j -= 1
    return j + 1


def quicksort(A: list, L: int, r: int) -> None:
    if (r - L <= 1):
        return
    q = partition(A, L, r)
    quicksort(A, L, q)
    quicksort(A, q, r)


def cnt_elems(a: list) -> int:
    c = 1
    for i in range(len(A) - 1):
        if A[i] != A[i+1]:
            c += 1
    return c


N = int(input())
A = list(map(int, input().split()))
quicksort(A, 0, N)
print(cnt_elems(A))
