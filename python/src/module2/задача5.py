def quick_sort(listik):
    if len(listik) <= 1:
        return listik
    ciferka = listik[len(listik) // 2]
    l = [i for i in listik if i < ciferka]
    m = [i for i in listik if i == ciferka]
    r = [i for i in listik if i > ciferka]
    result = quick_sort(l) + m + quick_sort(r)
    return result


def duplicate(arr):
    arr = quick_sort(arr)
    result = []
    for i in range(len(arr)):
        if (i == 0) or (arr[i] != arr[i-1]):
            result.append(arr[i])
    return result


A = int(input())
if A == 1:
    listik = int(input())
    print(listik)
else:
    listik = list(map(int, input().split()))
    listik = duplicate(listik)
    print(len(listik))