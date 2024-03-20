#Сортировка слиянием с выводом границ

a = int(input())
s = input().split()
mas= []
for i in range(a):
    mas.append(int(s[i]))

def mergeArr(first, second, start):
    result = []
    curr1 = 0
    curr2 = 0
    for i in range(len(first) + len(second)):
        if (curr2 == len(second) or (curr1 < len(first) and first[curr1] <= second[curr2])):
            result.append(first[curr1])
            curr1 += 1
        else:
            result.append(second[curr2])
            curr2 += 1
    print(str(start + 1) + " " + str(start + len(result)) + " " + str(result[0]) + " " + str(result[len(result) - 1]))
    return result

def mergeSort(input, start, end):
    if (end - start == 1):
        return [input[start]]
    middle = int((start + end) // 2)
    firstHalf = mergeSort(input, start, middle)
    secondHalf = mergeSort(input, middle, end)
    return mergeArr(firstHalf, secondHalf, start)

mas = mergeSort(mas, 0, len(mas))

print(" ".join(map(str, mas)))