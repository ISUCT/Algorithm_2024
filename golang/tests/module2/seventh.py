## Неправильно
def counting(mas, pos):
    key1 = min([int(x[pos]) for x in mas])
    key2 = max([int(x[pos]) for x in mas])
    n = key2 - key1 + 1
    support = [0 for i in range(n)]
    for el in mas:
        support[int(el[pos]) - key1] += 1
    size = len(mas)
    for i in range(n - 1, -1, -1):
        size -= support[i]
        support[i] = size
    result = [None for i in range(len(mas))]
    for el in mas:
        result[support[int(el[pos]) - key1]] = el
        support[int(el[pos]) - key1] += 1
    return result

    
def every_phase(mas, pos):
    print(f'Phase {abs(pos)}')
    for i in range(10):
        check = [x for x in mas if int(x[pos]) == i]
        print(f'Basket {i}:', end=' ')
        if len(check) > 0:
            print(*check, sep=', ')
        else:
            print('empty')
        
def r_sort(mas):
    mas_digs = len(mas[0])
    for i in range(-1, -(mas_digs) - 1, -1):
        mas = counting(mas, i)
        every_phase(mas, i)
        print('*' * 10)
    print("Array:")
    print(*mas, sep=", ")


if __name__ == "__main__":
    a = int(input())
    if a == 1:
        mas = input()
        print("Initial array:")
        print(*mas, sep=", ")
        print('*' * 10)
        r_sort(mas)
    else:
        mas = [input() for _ in range(a)]
        print("Initial array:")
        print(*mas, sep=", ")
        print('*' * 10)
        r_sort(mas)