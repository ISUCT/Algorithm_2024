def radix_sort(arr):

    max_len = max(len(s) for s in arr)

    arr = [s.zfill(max_len) for s in arr]

    for i in range(max_len-1, -1, -1):
        buckets = [[] for _ in range(10)]

        for s in arr:
            digit = int(s[i])
            buckets[digit].append(s)

        print(f"Phase {max_len-i}")
        for j in range(10):
            if not buckets[j]:
                print(f"Bucket {j}: empty")
            else:
                print(f"Bucket {j}: {', '.join(buckets[j])}")

        arr = [s for bucket in buckets for s in bucket]
        print("**********")

    return arr


n = int(input())
arr = [input() for _ in range(n)]


print("Initial array:")
print(", ".join(arr))
print("**********")

sorted_array = radix_sort(arr)

print("Sorted array:")
print(", ".join(sorted_array))
