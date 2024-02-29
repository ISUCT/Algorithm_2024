# Utils
def check_swipe_requirement(
    record_current: list[int], record_to_swipe: list[int]
) -> bool:
    price_current = record_current[1]
    price_to_check = record_to_swipe[1]

    if price_current == price_to_check:
        id_current = record_current[0]
        id_to_check = record_to_swipe[0]
        return id_to_check > id_current
    else:
        return price_to_check < price_current


# Program start
total_count = int(input())
records = [None] * total_count  # type: list[list[int] | None]

# Read & sort 'at the run'
for outer_index in range(total_count):
    record_to_insert = list(map(int, input().split(" ")))
    inner_index = outer_index - 1
    while inner_index >= 0 and check_swipe_requirement(
        record_to_insert, records[inner_index]  # type: ignore
    ):
        records[inner_index + 1] = records[inner_index]
        inner_index -= 1
    records[inner_index + 1] = record_to_insert

# Output
for record in records:
    print(record[0], record[1])  # type: ignore
