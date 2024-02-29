totals = int(input())
elements = list(map(int, input().split(" ")))

no_swipes_were_made = True
for outer_index in range(len(elements) - 1, 0, -1):
    list_is_sorted = True
    for inner_index in range(outer_index):
        if elements[inner_index] > elements[inner_index + 1]:
            elements[inner_index], elements[inner_index + 1] = (
                elements[inner_index + 1],
                elements[inner_index],
            )
            list_is_sorted = False
            no_swipes_were_made = False
            print(*elements)
    if list_is_sorted:
        break

if no_swipes_were_made:
    print(0)
