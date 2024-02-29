# Utils
def read_words():
    return (int(i) for i in input().split(" ") if i.strip() != "")


def read_ints():
    return map(int, read_words())


# Input
count_of_kinds = int(input())
kinds_at_storage = list(read_ints())

count_of_user_orders = int(input())
user_orders = read_ints()

# Summarization
summarized_user_orders = [0] * count_of_kinds

for _ in range(count_of_user_orders):
    current_order = next(user_orders) - 1  # Index correction
    summarized_user_orders[current_order] += 1

# Result calculation
for kind_index in range(count_of_kinds):
    print(
        "yes"
        if kinds_at_storage[kind_index] < summarized_user_orders[kind_index]
        else "no"
    )
