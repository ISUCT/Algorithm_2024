def quick(array):
    if len(array) <= 1:
        return array
    a = array[len(array) // 2]
    lt = [x for x in array if x < a]
    mid = [x for x in array if x == a]
    rt = [x for x in array if x > a]
    return quick(lt) + mid + quick(rt)

def remove_duplicates(array):
    array = quick(array)
    res = []
    for i in range(len(array)):
        if i == 0 or array[i] != array[i-1]:
            res.append(array[i])
    return res

if __name__ == "__main__":
    b = int(input())
    if b == 1:
        c = int(input())
        print(c)
    else:
        c = list(map(int, input().split()))
        c = remove_duplicates(c)
        print(len(c))