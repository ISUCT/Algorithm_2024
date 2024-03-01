def counting_sort(listik, position):
    mini = min([int(x[position]) for x in listik])
    maxi = max([int(x[position]) for x in listik])
    number = maxi - mini + 1
    support = [0 for i in range(number)]
    for elem in listik:
        support[int(elem[position]) - mini] = support[int(elem[position]) - mini] + 1
    size = len(listik)
    for i in range(number - 1, -1, -1):
        size = size - support[i]
        support[i] = size
    result = [None for i in range(len(listik))]
    for elem in listik:
        result[support[int(elem[position]) - mini]] = elem
        support[int(elem[position]) - mini] = support[int(elem[position]) - mini] + 1
    return result

    
def print_phase(listik, position):
    print('Phase ' + str(abs(position)))
    for i in range(10):
        check= [x for x in listik if int(x[position]) == i]
        print(f'Bucket {i}:', end=' ')
        if len(check) > 0:
            print(*check, sep=', ')
        else:
            print('empty')
        
def radix_sort(listik):
    digits_num = len(listik[0])
    for i in range(-1, -(digits_num) - 1, -1):
        listik = counting_sort(listik, i)
        print_phase(listik, i)
        print('*' * 10)
    print("Sorted array:")
    print(*listik, sep=", ")



A = int(input())
if A == 1:
    listik = input()
    print("Initial array:")
    print(*listik, sep=", ")
    print('*' * 10)
    radix_sort(listik)
else:
    listik = [input() for _ in range(A)]
    print("Initial array:")
    print(*listik, sep=", ")
    print('*' * 10)
    radix_sort(listik)