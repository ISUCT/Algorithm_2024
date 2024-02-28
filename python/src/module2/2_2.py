def print_array(a: list):
    for i in a:
        print(*i, sep=' ')


N = int(input())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
for i in range(N):
    for j in range(0, N - i-1):
        q = list(a[j])
        if a[j][1] < a[j+1][1]:
            a[j] = a[j+1]
            a[j+1] = q
        if a[j][1] == a[j+1][1] and a[j][0] > a[j+1][0]:
            a[j] = a[j+1]
            a[j+1] = q
print_array(a)
