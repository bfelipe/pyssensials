def reminder_hash(number: int, table_size: int):
    return number % table_size


def folding_hash(number: int, table_size: int):
    pairs = []
    number_str = str(number)

    if len(number_str) % 2 != 0:
        number_str = number_str + '0'

    number = int(number_str)

    while number > 0:
        pair = number % 100
        pairs.insert(0, pair)
        number //= 100

    total_pairs = sum(pairs)
    return total_pairs % table_size


def reversed_folding_hash(number: int, table_size: int):
    pairs = []
    number_str = str(number)

    if len(number_str) % 2 != 0:
        number_str = number_str + '0'

    mid_numbers = number_str[1:-1]
    reversed_mid_numbers = mid_numbers[::-1]
    number_str = number_str[0] + reversed_mid_numbers + number_str[-1]

    number = int(number_str)

    while number > 0:
        pair = number % 100
        pairs.insert(0, pair)
        number //= 100

    total_pairs = sum(pairs)
    return total_pairs % table_size


def mid_square_hash(number: int, table_size: int):
    number **= 2
    number_str = str(number)
    middle = 0 + len(number_str) // 2
    token = number_str[middle - 1] + number_str[middle]
    return int(token) % table_size
