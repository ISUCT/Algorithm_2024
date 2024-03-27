def f(array):
    v = len(array)
    s = 0
    for i in range(v - 1):
        for j in range(v - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                s += 1
                print(*array)
    if s == 0:
        print(0)

V = int(input())
array = list(map(int, input().split()))
f(array)