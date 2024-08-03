def bubble_sort(items):
    num_passes = len(items) - 1
    while num_passes > 0:
        index = 0
        while index < num_passes:
            if items[index] > items[index + 1]:
                _swap(items, index, index + 1)
            index += 1
        num_passes -= 1


def selection_sort(items):
    last_position = len(items) - 1
    while last_position > 0:
        max_position = 0
        position = 1
        while position <= last_position:
            if items[position] > items[max_position]:
                max_position = position
            position += 1

        _swap(items, last_position, max_position)
        last_position -= 1


def insertion_sort(items):
    index = 1
    while index <= len(items) - 1:
        current = items[index]
        position = index

        while position > 0 and items[position - 1] > current:
            items[position] = items[position - 1]
            position -= 1

        items[position] = current
        index += 1


def shell_sort(items):
    sublist_count = len(items) // 2
    while sublist_count > 0:
        start_position = 0
        while start_position < sublist_count:
            _gap_insertion_sort(items, start_position, sublist_count)
            start_position += 1

        sublist_count = sublist_count // 2


def _gap_insertion_sort(items, start, gap):
    index = start + gap
    while index < len(items):
        current_value = items[index]
        position = index

        while position >= gap and items[position - gap] > current_value:
            items[position] = items[position - gap]
            position = position - gap

        items[position] = current_value
        index += gap


def merge_sort(items):
    if len(items) > 1:
        mid = len(items) // 2
        left_half = [0] * mid
        right_half = [0] * (len(items) - mid)

        left_index = 0
        while left_index < mid:
            left_half[left_index] = items[left_index]
            left_index += 1

        right_index = mid
        while right_index < len(items):
            right_half[right_index - mid] = items[right_index]
            right_index += 1

        merge_sort(left_half)
        merge_sort(right_half)

        merge_index = 0
        left_index = 0
        right_index = 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                items[merge_index] = left_half[left_index]
                left_index += 1
            else:
                items[merge_index] = right_half[right_index]
                right_index += 1
            merge_index += 1

        while left_index < len(left_half):
            items[merge_index] = left_half[left_index]
            left_index += 1
            merge_index += 1

        while right_index < len(right_half):
            items[merge_index] = right_half[right_index]
            right_index += 1
            merge_index += 1


def quick_sort(items):
    _quick_sort_helper(items, 0, len(items) - 1)


def _quick_sort_helper(items, first, last):
    if first < last:
        split_point = _partition(items, first, last)
        _quick_sort_helper(items, first, split_point - 1)
        _quick_sort_helper(items, split_point + 1, last)


def _partition(items, first, last):
    pivot = items[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and items[left_mark] <= pivot:
            left_mark += 1

        while items[right_mark] >= pivot and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            _swap(items, left_mark, right_mark)

    _swap(items, first, right_mark)
    return right_mark


def _swap(items, current_index, next_index):
    temp = items[current_index]
    items[current_index] = items[next_index]
    items[next_index] = temp


def _heapify(data, heap_size, root_index):
    largest_index = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and data[left] > data[largest_index]:
        largest_index = left

    if right < heap_size and data[right] > data[largest_index]:
        largest_index = right

    if largest_index != root_index:
        data[root_index], data[largest_index] = data[largest_index], data[root_index]
        _heapify(data, heap_size, largest_index)


def heap_sort(data):
    heap_size = len(data)

    for start_index in range((heap_size//2)-1, -1, -1):
        _heapify(data, heap_size, start_index)

    for end_index in range(heap_size-1, 0, -1):
        data[end_index], data[0] = data[0], data[end_index]
        _heapify(data, end_index, 0)
