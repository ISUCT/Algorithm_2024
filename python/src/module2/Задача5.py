def quick_sort(a):
    if len(a) <= 1:
        return a
    num = a[len(a) // 2]
    left = [x for x in a if x < num]
    middle = [x for x in a if x == num]
    right = [x for x in a if x > num]
    return quick_sort(left) + middle + quick_sort(right)

def remove_duplicates(a):
    a = quick_sort(a)
    result = []
    for i in range(len(a)):
        if (i == 0) or (a[i] != a[i-1]):
            result.append(a[i])
    return result

if __name__ == "__main__":
    n = int(input())
    if n == 1:
        lst = int(input())
        print(lst)
    else:
        lst = list(map(int, input().split()))
    
        lst = remove_duplicates(lst)
        print(len(lst))