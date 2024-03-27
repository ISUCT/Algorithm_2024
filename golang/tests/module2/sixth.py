def count_sort(prod, max_orders):
    answer = []   
    min_val = min(prod)
    max_val = max(prod)
    support = [0 for j in range(max_val - min_val + 1)]
    for el in prod:
        support[el - min_val] += 1
    
    for j in range(len(support)):
        if support[j] <= max_orders[j]:
            answer.append('no')
        else:
            answer.append('yes')
    
    for result in answer:
        print(result)


if __name__ == "__main__":
    products_in = int(input())           
    products = list(map(int, input().split()))
    orders = int(input())
    orders_in = list(map(int, input().split()))
    count_sort(orders_in, products)