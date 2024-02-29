# Utils
def read_words():
    return list(input().strip() for i in range(int(input())))


items = read_words()

# print initial
print("Initial array:")
print(*items, sep=", ")

# sorting process
buckets = [[] for _ in range(10)]  # type: list[list[str]]

# We could take any of itmes to take rank count.
# Length of each item is same.
rank_count = len(items[0])

for rank_num in range(rank_count):
    print("**********")
    # bucket calculation
    for item in items:
        rank_value = item[rank_count - rank_num - 1]
        rank_value = ord(rank_value) - ord("0")
        buckets[rank_value].append(item)

    items = []
    # print & order recalulation

    print("Phase", str(rank_num + 1))

    for index, bucket in enumerate(buckets):
        print(f"Bucket {index}: ", end="")
        if bucket:
            print(*bucket, sep=", ")
        else:
            print("empty")

        for item in bucket:
            items.append(item)

        buckets[index] = []

# print sorted
print("**********")
print("Sorted array:")
print(*items, sep=", ")
