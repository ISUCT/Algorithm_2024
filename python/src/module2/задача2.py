def sortirovka(A):
    number = list()
    cost = list()
    for i in range(A):
        listik = list(map(int, input().split()))
        number.append(listik[0])
        cost.append(listik[-1])
    
    for i in range(A- 1):
        for j in range(A - 1):
            if cost[j] == cost[j + 1]:
                if number[j] < number[j + 1]:
                    cost[j], cost[j + 1] = cost[j + 1], cost[j]
                    number[j], number[j + 1] = number[j + 1], number[j]
            else:
                if cost[j] > cost[j + 1]:
                    cost[j], cost[j + 1] = cost[j + 1], cost[j]
                    number[j], number[j + 1] = number[j + 1], number[j]
    
    for i in range(A - 1, -1, -1):
        print(str(number[i]) + " " + str(cost[i]))
        
        

A = int(input())
if A == 1:
    listik = list(map(int, input().split()))
    print(*listik)
else:
    sortirovka(A) 