def get_max_length(arr):
    max_len = 0
    for item in arr:
        max_len = max(max_len, len(item))
    return max_len

def distribute_to_bins(arr, bins, digit):
    for item in arr:
        value = item if len(item) > digit else "0" * digit + item
        bins[int(value[-(digit+1)])].append(item)

def collect_from_bins(arr, bins):
    output = []
    for bin in bins:
        output.extend(bin)
    return output

def radix_sort(arr):
    bins = [[] for _ in range(10)]
    max_len = get_max_length(arr)
    print("Initial array:\n" + ", ".join(arr))
    for phase in range(max_len):
        print("**********")
        print(f"Phase {phase + 1}")
        distribute_to_bins(arr, bins, phase)
        for i in range(10):
            print(f"Bucket {i}: {', '.join(bins[i]) if bins[i] else 'empty'}")
        arr = collect_from_bins(arr, bins)
        bins = [[] for _ in range(10)]
    print("**********")
    print("Sorted array:\n" + ", ".join(arr))

n = int(input())
arr = [input() for i in range(n)]
radix_sort(arr)