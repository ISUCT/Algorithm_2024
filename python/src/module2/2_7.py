def radix_sort(arr):
    len_digits = max(len(num) for num in arr)
    for i in range(len_digits):
        b = [[] for _ in range(10)]
        for x in arr:
            b[(int(x) // 10 ** i) % 10].append(x)
        print("Phase", i)
        for j in range(10):
            print(f"Bucket {j}:", ', '.join(b[j]) if b[j] else 'empty')
        print("**********")
        arr = [num for bucket in b for num in bucket]
    return arr


n = int(input())
arr = [input().strip() for _ in range(n)]
print("Initial array:")
print(', '.join(arr))
print("**********")
sorted_arr = radix_sort(arr)
print("Sorted array:")
print(', '.join(sorted_arr))
