#Сортировка пузырьком

n=int(input())
count=0
mas=list(map(int, (input().split())))
for i in range(n-1):
             for j in range(n-i-1):
              if mas[j] > mas[j+1]:
               mas[j], mas[j+1] = mas[j+1], mas[j]
               count+=1
               print(" ".join(map(str, mas)))
if count==0:
 print((0))