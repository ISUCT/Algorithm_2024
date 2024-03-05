def purchase_automation():
    types = int(input())
    storage = list(map(int, input().split()))
    total = int(input())
    orders = list(map(int, input().split()))

    orders_count = {}
    for order in orders:
        if order in orders_count:
            orders_count[order] += 1
        else:
            orders_count[order] = 1

    search_result = []
    for item in range(types):
        if item + 1 in orders_count:
            if storage[item] < orders_count[item+1]:
                search_result.append("yes")
            else:
                search_result.append("no")
        else:
            search_result.append("no")

    return search_result

output = purchase_automation()
for line in output:
    print(line)
