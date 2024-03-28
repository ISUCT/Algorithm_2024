def mergesort(l, r):
    return sorted(l + r)

def merge_two(arr, left, right):
    if right - left <= 1:
        return arr[left:right]
    
    mid = (left + right) // 2
    l = merge_two(arr, left, mid)
    r = merge_two(arr, mid, right)
    m = mergesort(l, r)
    print(f"{left + 1} {right} {m[0]} {m[-1]}")
    return m

if __name__ == "__main__":
    s = int(input())
    arr = list(map(int, input().split()))
    s_arr = merge_two(arr, 0, s)
    print(" ".join(map(str, s_arr)))