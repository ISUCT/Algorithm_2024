def sortr(list):
    cor = [[] for _ in range(10)]
    mlen = max(len(x) for x in list)
    print("Initial array:\n" + ", ".join(list))
    for p in range(mlen):
        print("**********")
        print(f"Phase {p + 1}")
        for i in range(10):
            for l in list:
                if len(l) > p:
                    if int(l[-p-1]) == i:
                        cor[i].append(l)
            print(f"Bucket {i}: {', '.join(cor[i]) if cor[i] else 'empty'}")

        list = [x for b in cor for x in b]
        cor = [[] for _ in range(10)]

    print("**********")
    print("Sorted array:\n" + ", ".join(list))

n = int(input())
list = [input() for _ in range(n)]
sortr(list)