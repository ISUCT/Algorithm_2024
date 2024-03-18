len_death = int(input())
arrey_number = []
arrey_cost = []
for i in range (0, len_death, 1):
    thing = input()
    thing = thing.split()
    thing[0] = int(thing[0])
    arrey_number.append(thing[0])
    thing[-1] = int(thing[-1])
    arrey_cost.append(thing[-1])
for i in range(0, len_death-1, 1):
    for j in range(0, len_death-1, 1):
        if int(arrey_cost[j]) == arrey_cost[j + 1]:
            if int(arrey_number[j]) < arrey_number[j + 1]:
                arrey_cost[j], arrey_cost[j + 1] = arrey_cost[j + 1], arrey_cost[j]
                arrey_number[j], arrey_number[j + 1] = arrey_number [j + 1], arrey_number[j]
        else:
            if int(arrey_cost[j]) > arrey_cost[j + 1]:
                arrey_cost[j], arrey_cost[j + 1] = arrey_cost[j + 1], arrey_cost[j]
                arrey_number[j], arrey_number[j + 1] = arrey_number[j + 1], arrey_number[j]
for i in range(len_death-1, -1, -1):
    print(str(arrey_number[i])+" "+str(arrey_cost[i]))
