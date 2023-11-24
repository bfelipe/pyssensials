import collections
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

    def test_hash_map(self):
        with self.assertRaises(collection.InvalidTableSizeError):
            collection.HashMap(1024)

        hm = collection.HashMap()
        assert type(hm) is collection.HashMap
        assert hm.is_empty() is True
        assert hm.size() == 0
        assert hm.capacity() == 499
        assert hm.contains('cat') is False
        assert hm.contains(123) is False
        assert hm.get('cat') is None
        assert hm.get(123) is None
        hm.put('cat', 54)
        hm.put('dog', 26)
        hm.put('lion', 93)
        hm.put('tiger', 17)
        hm.put('bird', 77)
        hm.put('cow', 31)
        hm.put(44, 'goat')
        hm.put(55, 'pig')
        hm.put(20, 'chicken')
        assert hm.is_empty() is False
        assert hm.size() == 9
        assert hm.get('cat') == 54
        assert hm.get('dog') == 26
        assert hm.get('lion') == 93
        assert hm.get('tiger') == 17
        assert hm.get('bird') == 77
        assert hm.get('cow') == 31
        assert hm.get(44) == 'goat'
        assert hm.get(55) == 'pig'
        assert hm.get(20) == 'chicken'
        hm.put('cat', 100)
        hm.put(44, 'medusa')
        assert hm.get('cat') == 100
        assert hm.get(44) == 'medusa'
        hm.delete('cat')
        hm.delete(44)
        assert hm.get('cat') is None
        assert hm.get(44) is None
        assert hm.size() == 7
        hm.delete('dog')
        hm.delete('lion')
        hm.delete('tiger')
        hm.delete('bird')
        hm.delete('cow')
        hm.delete(55)
        hm.delete(20)
        assert hm.get('dog') is None
        assert hm.get('lion') is None
        assert hm.get('tiger') is None
        assert hm.get('bird') is None
        assert hm.get('cow') is None
        assert hm.get(55) is None
        assert hm.get(20) is None
        assert hm.size() == 0

    def test_min_binary_heap(self):
        h = collection.Heap()
        assert type(h) is collection.Heap
        assert h.is_empty() is True
        assert h.size() == 0

        data = [9, 6, 5, 2, 3]

        h.build(data)
        assert h.is_empty() is False
        assert h.size() == 5
        assert h.find_min() == 2
        h.clear()
        assert h.is_empty() is True
        assert h.size() == 0
        for item in data:
            h.insert(item)
        assert h.is_empty() is False
        assert h.size() == 5
        for _ in data:
            min_val = h.find_min()
            assert h.remove_min() == min_val
        assert h.is_empty() is True
        assert h.size() == 0
