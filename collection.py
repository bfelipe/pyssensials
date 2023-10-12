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


class HashMap:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def capacity(self):
        pass

    def contains(self, key):
        pass

    def __repr__(self):
        pass
