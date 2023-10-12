import unittest

import collection


class CollectionTestCase(unittest.TestCase):

    def test_stack(self):
        s = collection.Stack()
        assert type(s) is collection.Stack
        assert s.is_empty() is True
        assert s.peek() == -1
        assert s.pop() == -1
        s.push(4)
        s.push('dog')
        assert s.peek() == 'dog'
        s.push(True)
        assert s.size() == 3
        assert s.is_empty() is False
        s.push(8.4)
        assert s.pop() == 8.4
        assert s.pop() is True
        assert s.size() == 2

    def test_queue(self):
        q = collection.Queue()
        assert type(q) is collection.Queue
        assert q.is_empty() is True
        assert q.dequeue() == -1
        q.enqueue(4)
        q.enqueue('dog')
        q.enqueue(True)
        assert q.size() == 3
        assert q.is_empty() is False
        q.enqueue(8.4)
        assert q.dequeue() == 4
        assert q.dequeue() == 'dog'
        assert q.size() == 2

    def test_deque(self):
        d = collection.Deque()
        assert type(d) is collection.Deque
        assert d.is_empty() is True
        assert d.remove_front() == -1
        assert d.remove_rear() == -1
        d.add_rear(4)
        d.add_rear('dog')
        d.add_front('cat')
        d.add_front(True)
        assert d.size() == 4
        assert d.is_empty() is False
        d.add_rear(8.4)
        assert d.remove_rear() == 8.4
        assert d.remove_front() is True

    def test_unordered_list(self):
        n = collection.Node(31)
        assert type(n) is collection.Node
        ul = collection.UnorderedList()
        assert type(ul) is collection.UnorderedList
        assert ul.is_empty() is True
        assert ul.remove(31) == -1
        assert ul.search(31) is False
        assert ul.index(31) == -1
        assert ul.pop() == -1
        assert ul.pop_at(0) == -1
        ul.add(31)
        ul.add(77)
        ul.add(17)
        ul.add(93)
        ul.add(26)
        ul.add(54)
        assert ul.size() == 6
        assert ul.search(26) is True
        assert ul.search(99) is False
        assert ul.index(93) == 2
        ul.insert(2, 123)
        assert ul.index(123) == 2
        assert ul.size() == 7
        ul.remove(123)
        assert ul.search(123) is False
        assert ul.index(93) == 2
        ul.insert(7, 123)
        assert ul.search(123) is False
        assert ul.search(31) is True
        assert ul.size() == 6
        assert ul.pop() == 31
        assert ul.search(31) is False
        assert ul.size() == 5
        assert ul.pop_at(7) == -1
        assert ul.pop_at(0) == 54
        assert ul.pop_at(1) == 93
        assert ul.pop_at(2) == 77
        assert ul.pop() == 17
        assert ul.pop() == 26
        assert ul.pop() == -1
        assert ul.pop_at(0) == -1

    def test_ordered_list(self):
        ol = collection.OrderedList()
        assert type(ol) is collection.OrderedList
        assert ol.is_empty() is True
        assert ol.size() == 0
        assert ol.remove(1) == -1
        assert ol.search(1) is False
        assert ol.index(1) == -1
        assert ol.pop() == -1
        assert ol.pop_at(2) == -1
        ol.add(31)
        ol.add(77)
        ol.add(17)
        ol.add(93)
        ol.add(26)
        ol.add(54)
        assert ol.is_empty() is False
        assert ol.size() == 6
        assert ol.search(31) is True
        assert ol.index(93) == 5
        assert ol.pop() == 93
        assert ol.pop_at(1) == 26
        assert ol.pop() == 77
        assert ol.pop() == 54
        assert ol.pop_at(1) == 31
        assert ol.pop() == 17
        assert ol.pop() == -1
        assert ol.pop_at(0)
        assert ol.is_empty() is True
        assert ol.size() == 0
