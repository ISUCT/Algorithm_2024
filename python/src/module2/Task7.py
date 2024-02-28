def radix_sort(list):
    bins = [[] for _ in range(10)]
    maxlen = max(len(x) for x in list)
    print("Initial array:\n" + ", ".join(list))
    for phase in range(maxlen):
        print("**********")
        print(f"Phase {phase + 1}")
        for i in range(10):
            for el in list:
                if len(el) > phase:
                    if int(el[-phase-1]) == i:
                        bins[i].append(el)
            print(f"Bucket {i}: {', '.join(bins[i]) if bins[i] else 'empty'}")

        list = [x for b in bins for x in b]
        bins = [[] for _ in range(10)]

    print("**********")
    print("Sorted array:\n" + ", ".join(list))

n = int(input())
list = [input() for _ in range(n)]
radix_sort(list)