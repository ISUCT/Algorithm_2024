N = int(input())
a = list(map(int, input().split()))


def buble_sort(a):
    a1 = list(a)
    for i in range(N):
        for j in range(0, N - i-1):
            q = a[j]
            if a[j] > a[j+1]:
                a[j] = a[j+1]
                a[j+1] = q
                print(*a)
    if a1 == a:
        print(0)


buble_sort(a)
