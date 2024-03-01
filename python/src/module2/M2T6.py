def read_input():
    n = int(input())
    stock = list(map(int, input().split()))
    k = int(input())
    orders = list(map(int, input().split()))
    return n, stock, k, orders


def process_orders(n, stock, k, orders):
    order_count = [0] * n
    for order in orders:
        order_count[order - 1] += 1

    for i in range(n):
        if stock[i] < order_count[i]:
            print('yes')
        else:
            print('no')


def res():
    n, stock, k, orders = read_input()
    process_orders(n, stock, k, orders)


res()
