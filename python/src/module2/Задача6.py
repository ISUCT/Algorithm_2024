def count_sort(lst, check_lst):
    a = []   
    min_value = min(lst)
    max_value = max(lst)
    support = [0 for i in range(max_value - min_value + 1)]
    for element in lst:
        support[element - min_value] += 1
    
    for j in range(len(support)):
        if support[j] <= check_lst[j]:
            a.append('no')
        else:
            a.append('yes')
    
    for i in a:
        print(i)


if __name__ == "__main__":
    goods = int(input())           
    amount_product = list(map(int, input().split()))
    amount_of_orders = int(input())
    customer_orders = list(map(int, input().split()))
    count_sort(customer_orders, amount_product)