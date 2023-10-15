import hashing

class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return -1
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __repr__(self):
        tokens = []
        for index, item in enumerate(self.items):
            if index == 0:
                tokens.append('Base: %s' % item)
            elif index == self.size() - 1:
                tokens.append('Top: %s' % item)
            else:
                tokens.append(item)
        return ' -> '.join(tokens)


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            return - 1
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)


class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, data):
        self.items.insert(0, data)

    def add_rear(self, data):
        self.items.append(data)

    def remove_front(self):
        if self.is_empty():
            return -1
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return -1
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return str(self.data)


class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data, self.head)
        self.head = node

    def remove(self, data):
        if self.is_empty():
            return -1

        current = self.head
        previous = None
        found = False

        while not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next_node

        # if previous is None means the item to be removed
        # is the second node, so previous didnt changed to current
        if previous is None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node

    def search(self, data):
        found = False

        if self.is_empty():
            return found

        current = self.head
        stop = False

        while not stop:
            if current:
                if current.data == data:
                    found = True
                    stop = True
                else:
                    current = current.next_node
            else:
                stop = True

        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        counter = 0
        current = self.head
        while current:
            current = current.next_node
            counter += 1
        return counter

    def append(self, data):
        if self.is_empty():
            self.add(data)
            return

        current = self.head
        stop = False

        while not stop:
            if current.next_node is None:
                stop = True
            else:
                current = current.next_node

        current.next_node = Node(data)

    def index(self, data):
        if self.is_empty():
            return -1

        current = self.head
        position = 0
        found = False

        while current and not found:
            if current.data == data:
                found = True
            else:
                current = current.next_node
                position += 1

        if found:
            return position
        return -1

    def insert(self, index, data):
        if self.size() < index:
            return

        if index == 0:
            self.add(data)
            return

        position = 0
        current = self.head
        previous = None
        stop = False

        while not stop:
            if position == index:
                previous.next_node = Node(data, current)
                stop = True
            else:
                position += 1
                previous = current
                current = current.next_node

    def pop(self):
        if self.is_empty():
            return -1

        current = self.head
        previous = None
        stop = False

        while not stop:
            if previous is None and current.next_node is None:
                self.head = None
                stop = True
            elif previous and current.next_node is None:
                previous.next_node = None
                stop = True
            else:
                previous = current
                current = current.next_node

        return current.data

    def pop_at(self, index):
        if self.size() < index:
            return -1

        if self.is_empty():
            return -1
        current = self.head

        if index == 0:
            self.head = current.next_node
            return current.data

        position = 1
        previous = current
        current = current.next_node
        stop = False

        while not stop:
            if current:
                if position == index:
                    previous.next_node = current.next_node
                    return current.data
                else:
                    position += 1
                    previous = current
                    current = current.next_node
            else:
                stop = True
        return -1

    def __repr__(self):
        if self.is_empty():
            return 'Head: None -> Tail: None'
        result = []
        current = self.head
        while current:
            if current == self.head:
                result.append('Head: [%s]' % str(current.data))
            elif current.next_node is None:
                result.append('Tail: [%s]' % str(current.data))
            else:
                result.append('[%s]' % str(current.data))
            current = current.next_node
        return ' -> '.join(result)


class OrderedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.data > data:
                stop = True
            else:
                previous = current
                current = current.next_node

        node = Node(data)
        if previous is None:
            node.next_node = self.head
            self.head = node
        else:
            node.next_node = current
            previous.next_node = node

    def remove(self, data):
        if self.is_empty():
            return -1

        current = self.head
        previous = None
        found = False

        while not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next_node

        # if previous is None means the item to be removed
        # is the second node, so previous didnt changed to current
        if previous is None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node

    def search(self, data):
        found = False

        if self.is_empty():
            return found

        current = self.head
        stop = False

        while not stop:
            if current:
                if current.data == data:
                    found = True
                    stop = True
                elif current.data > data:
                    stop = True
                else:
                    current = current.next_node
            else:
                stop = True

        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        counter = 0
        current = self.head
        while current:
            current = current.next_node
            counter += 1
        return counter

    def index(self, data):
        if self.is_empty():
            return -1

        current = self.head
        position = 0
        found = False

        while current and not found:
            if current.data == data:
                found = True
            else:
                current = current.next_node
                position += 1

        if found:
            return position
        return -1

    def pop(self):
        if self.is_empty():
            return -1

        current = self.head
        previous = None
        stop = False

        while not stop:
            if previous is None and current.next_node is None:
                self.head = None
                stop = True
            elif previous and current.next_node is None:
                previous.next_node = None
                stop = True
            else:
                previous = current
                current = current.next_node

        return current.data

    def pop_at(self, index):
        if self.size() < index:
            return -1

        if self.is_empty():
            return -1
        current = self.head

        if index == 0:
            self.head = current.next_node
            return current.data

        position = 1
        previous = current
        current = current.next_node
        stop = False

        while not stop:
            if current:
                if position == index:
                    previous.next_node = current.next_node
                    return current.data
                else:
                    position += 1
                    previous = current
                    current = current.next_node
            else:
                stop = True
        return -1

    def __repr__(self):
        if self.is_empty():
            return 'Head: None -> Tail: None'
        result = []
        current = self.head
        while current:
            if current == self.head:
                result.append('Head: [%s]' % str(current.data))
            elif current.next_node is None:
                result.append('Tail: [%s]' % str(current.data))
            else:
                result.append('[%s]' % str(current.data))
            current = current.next_node
        return ' -> '.join(result)


class InvalidTableSizeError(Exception):
    pass


class HashMap:
    """
        In this implementation we are using probing technique to allocate
        each key/value in a unique slot.
        Keep in mind that if the load factor (λ) is small, collisions is also
        have a small chance to occur.

        Load factor: λ = number_of_item / stable_size

        When a load factor is large (close to the table_size), collisions are
        more prone to occur, this make a new hash (index) to be calculated.
        If you are about to clear the entire HashMap using delete() function
        you probably going to have weird behavior since you are more like to
        come across a None slot before reaching your desired one.

        It is recommended you make your load factor ALWAYS bigger than the number or
        key/value pairs.
    """
    def __init__(self, table_size: int = 499):
        self.table_size = self._check_table_size(table_size)
        self.keys = [None] * self.table_size
        self.values = [None] * self.table_size
        self.probe = 1

    @staticmethod
    def _to_ord(key):
        if type(key) is str:
            tokens = [str(ord(letter)) for letter in key]
            return int(''.join(tokens))
        return key

    def put(self, key, value):
        index = hashing.reminder_hash(self._to_ord(key), self.table_size)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            if self.keys[index] == key:
                self.values[index] = value
            else:
                index = hashing.reminder_hash(index + self.probe, self.table_size)
                while self.keys[index] is not None and self.keys[index] != key:
                    index = hashing.reminder_hash(index + self.probe, self.table_size)
                if self.keys[index] is None:
                    self.keys[index] = key
                    self.values[index] = value
                else:
                    self.values[index] = value

    def get(self, key):
        start_index = hashing.reminder_hash(self._to_ord(key), self.table_size)
        index = start_index
        value = None
        stop = False
        found = False
        while self.keys[index] is not None and not found and not stop:
            if self.keys[index] == key:
                value = self.values[index]
                found = True
            else:
                index = hashing.reminder_hash(index + self.probe, self.table_size)
                if index == start_index:
                    stop = True
        return value

    def delete(self, key):
        start_index = hashing.reminder_hash(self._to_ord(key), self.table_size)
        index = start_index
        stop = False
        found = False
        while self.keys[index] is not None and not found and not stop:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                found = True
            else:
                index = hashing.reminder_hash(index + self.probe, self.table_size)
                if index == start_index:
                    stop = True

    def is_empty(self):
        result = True
        position = 0
        stop = False
        while position <= len(self.keys) - 1 and not stop:
            if self.keys[position] is not None:
                result = False
                stop = True
            else:
                position += 1
        return result

    def size(self):
        total = 0
        for index, _ in enumerate(self.keys):
            if self.keys[index] is not None:
                total += 1
        return total

    def capacity(self):
        return self.table_size

    def contains(self, key):
        key = self._to_ord(key)
        start_index = hashing.reminder_hash(key, self.table_size)
        index = start_index
        stop = False
        found = False
        while self.keys[index] is not None and not found and not stop:
            if self.keys[index] == key:
                found = True
            else:
                index = hashing.reminder_hash(index + self.probe, self.table_size)
                if index == start_index:
                    stop = True
        return found

    @staticmethod
    def _check_table_size(table_size):
        is_prime = True
        start = 2

        while start <= table_size // 2:
            if table_size % start == 0:
                is_prime = False
                break
            else:
                start += 1

        if not is_prime:
            raise InvalidTableSizeError('Table size must be a prime number')
        return table_size

    def __repr__(self):
        if self.is_empty():
            return 'HashMap: []'
        items = []
        for i, _ in enumerate(self.keys):
            if self.keys[i] is not None:
                items.append('(key: %s, value: %s)' % (self.keys[i], self.values[i]))
        return 'HashMap: %s' % items
