def count_sort(listik, check):
    answers = []   
    mini = min(listik)
    maxi = max(listik)
    sup = [0 for i in range(maxi - mini + 1)]
    for elem in listik:
        sup[elem - mini] =  sup[elem - mini] + 1
    
    for i in range(len(sup)):
        if sup[i] <= check[i]:
            answers.append('no')
        else:
            answers.append('yes')
    
    for i in answers:
        print(i)



goods_types = int(input())           
each_product = list(map(int, input().split()))
orders_count = int(input())
orders = list(map(int, input().split()))
count_sort(orders, each_product)