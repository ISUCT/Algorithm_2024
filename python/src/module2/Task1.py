n = int(input())
list = [int(num) for num in input().split()] 
count = 0
for el in range(n-1):
    for i in range(n-1):
        if list[i] > list[i+1]:
            count +=1
            list[i], list[i+1] = list[i+1], list[i]
            print(' '.join(map(str, list)))
if count == 0:
    print(0)