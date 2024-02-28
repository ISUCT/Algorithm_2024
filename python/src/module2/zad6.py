idT = int(input())
TovarList = [int(num) for num in input().split()] 
NumberCustomes = int(input())
CustomesList = [int(num) for num in input().split()] 
count_list = [0]*(idT+1)
for i in CustomesList:
    count_list[i] += 1
count_list.pop(0)
stopC = 0
while stopC < idT:
    if count_list[stopC] > TovarList[stopC]:
        print("yes")
    else:
        print("no")
    stopC += 1
