#Количество различных

num=int(input())
mas=list(map(int, (input().split())))
slovar = dict(zip(mas,mas))
print(len(slovar))