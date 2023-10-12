def ordered_linear(target, items: list):
    position = 0
    found = False
    stop = False

    while position < len(items) and not stop:
        if items[position] > target:
            stop = True
        elif items[position] == target:
            found = True
            stop = True
        else:
            position += 1
    return found


def unordered_linear(target, items: list):
    position = 0
    found = False
    stop = False

    while position < len(items) and not stop:
        if items[position] == target:
            found = True
            stop = True
        else:
            position += 1
    return found


def binary(target, items: list):
    start = 0
    end = len(items) - 1
    found = False

    while start <= end:
        middle = (start + end) // 2
        if items[middle] == target:
            found = True
        if items[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return found
