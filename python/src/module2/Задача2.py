def sort(a):
    numbers = list()
    cost_list = list()
    for i in range(a):
        s = list(map(int, input().split()))
        numbers.append(s[0])
        cost_list.append(s[-1])
    
    for i in range(a- 1):
        for j in range(a - 1):
            if cost_list[j] == cost_list[j + 1]:
                if numbers[j] < numbers[j + 1]:
                    cost_list[j], cost_list[j + 1] = cost_list[j + 1], cost_list[j]
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            else:
                if cost_list[j] > cost_list[j + 1]:
                    cost_list[j], cost_list[j + 1] = cost_list[j + 1], cost_list[j]
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    for i in range(a - 1, -1, -1):
        print(str(numbers[i]) + " " + str(cost_list[i]))
        
        
if __name__ == "__main__":
    a = int(input())
    if a == 1:
        lst = list(map(int, input().split()))
        print(*lst)
    else:
        sort(a)