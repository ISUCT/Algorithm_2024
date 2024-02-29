def counting_sort(lst, position):
    min_key = min([int(x[position]) for x in lst])
    max_key = max([int(x[position]) for x in lst])
    n = max_key - min_key + 1
    support = [0 for i in range(n)]
    for el in lst:
        support[int(el[position]) - min_key] += 1
    size = len(lst)
    for i in range(n - 1, -1, -1):
        size -= support[i]
        support[i] = size
    result = [None for i in range(len(lst))]
    for el in lst:
        result[support[int(el[position]) - min_key]] = el
        support[int(el[position]) - min_key] += 1
    return result

    
def print_each_phase(lst, position):
    print(f'Phase {abs(position)}')
    for i in range(10):
        check_list = [x for x in lst if int(x[position]) == i]
        print(f'Bucket {i}:', end=' ')
        if len(check_list) > 0:
            print(*check_list, sep=', ')
        else:
            print('empty')
        
def radix_sort(lst):
    number_of_digits = len(lst[0])
    for i in range(-1, -(number_of_digits) - 1, -1):
        lst = counting_sort(lst, i)
        print_each_phase(lst, i)
        print('*' * 10)
    print("Sorted array:")
    print(*lst, sep=", ")


if __name__ == "__main__":
    a = int(input())
    if a == 1:
        lst = input()
        print("Initial array:")
        print(*lst, sep=", ")
        print('*' * 10)
        radix_sort(lst)
    else:
        lst = [input() for _ in range(a)]
        print("Initial array:")
        print(*lst, sep=", ")
        print('*' * 10)
        radix_sort(lst)