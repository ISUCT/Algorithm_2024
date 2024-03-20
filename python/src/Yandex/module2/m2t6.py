#Склад

num = int(input())
mas = list(map(int, (input().split())))
buyers = int(input())
buy = list(map(int, (input().split())))
sell = [0]*num
for i in range(num):
    mas[i] = [mas[i], i+1]
for j in range(buyers):
    sell[buy[j] - 1] += 1
for n in mas:
    if n[0] < sell[n[1] - 1]:
        print("yes")
    else:
        print("no")