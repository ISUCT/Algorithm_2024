if __name__ == "__main__":
    n = int(input())
    goods_count = input().split()
    k = int(input())
    orders = input().split()
    for i in range(0,k):
        orders[i] = int(orders[i])
    for i in range(0,n):
        if orders.count(i+1) > int(goods_count[i]):
            print('yes')
        else:
            print('no')