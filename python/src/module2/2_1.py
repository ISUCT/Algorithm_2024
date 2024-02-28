def print_array(a):
    c = " "
    for i in a:
        c += str(i)
        c += " "
    print(c[1:-1])


N = int(input())
a = list(map(int, input().split()))
a1 = list(a)
for i in range(N):
    for j in range(0, N - i-1):
        q = a[j]
        if a[j] > a[j+1]:
            a[j] = a[j+1]
            a[j+1] = q
            print_array(a)
if a1 == a:
    print(0)
