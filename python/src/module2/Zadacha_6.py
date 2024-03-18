if __name__ == "__main__":
    len_thing = int(input())
    number = input().split()
    orders = int(input())
    orders_for_client = input().split()
    for i in range(0, orders):
        orders_for_client[i] = int(orders_for_client[i])
    for i in range(0, len_thing):
        if orders_for_client.count(i+1) > int(number[i]):
            print ("yes")
        else:
            print ("no")



