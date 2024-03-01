def radix_sort_merge(arr):
    max_len = max(len(num) for num in arr)
    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = int(num[i]) if i < len(num) else 0
            buckets[digit].append(num)

        print("Phase", max_len - i)
        for j in range(10):
            print(f"Bucket {j}:", ', '.join(buckets[j])
                  if buckets[j] else 'empty')
        print("**********")

        arr = [num for bucket in buckets for num in bucket]

    return arr


def main():
    n = int(input())
    arr = [input().strip() for _ in range(n)]

    print("Initial array:")
    print(', '.join(arr))
    print("**********")

    sorted_arr = radix_sort_merge(arr)

    print("Sorted array:")
    print(', '.join(sorted_arr))


if __name__ == "__main__":
    main()
