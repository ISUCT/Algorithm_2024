def count_sort(lst, check_lst):
    answer = []   
    min_value = min(lst)
    max_value = max(lst)
    support_list = [0 for i in range(max_value - min_value + 1)]
    for el in lst:
        support_list[el - min_value] += 1
    
    for j in range(len(support_list)):
        if support_list[j] <= check_lst[j]:
            answer.append('no')
        else:
            answer.append('yes')
    
    for i in answer:
        print(i)


if __name__ == "__main__":
    types_of_goods = int(input())           
    amount_of_each_product = list(map(int, input().split()))
    amount_of_orders = int(input())
    customer_orders = list(map(int, input().split()))
    count_sort(customer_orders, amount_of_each_product)