def sort(a):
    list_of_number = []
    list_of_cost = []
    for i in range(a):
        s = list(map(int, input().split()))
        list_of_number.append(s[0])
        list_of_cost.append(s[-1])
    
    for i in range(a- 1):
        for j in range(a - 1):
            if list_of_cost[j] == list_of_cost[j + 1]:
                if list_of_number[j] < list_of_number[j + 1]:
                    list_of_cost[j], list_of_cost[j + 1] = list_of_cost[j + 1], list_of_cost[j]
                    list_of_number[j], list_of_number[j + 1] = list_of_number[j + 1], list_of_number[j]
            else:
                if list_of_cost[j] > list_of_cost[j + 1]:
                    list_of_cost[j], list_of_cost[j + 1] = list_of_cost[j + 1], list_of_cost[j]
                    list_of_number[j], list_of_number[j + 1] = list_of_number[j + 1], list_of_number[j]
    
    for i in range(a - 1, -1, -1):
        print(f'{list_of_number[i]} {list_of_cost[i]}')
        
        
if __name__ == "__main__":
    a = int(input())
    if a == 1:
        lst = list(map(int, input().split()))
        print(*lst)
    else:
        sort(a) 