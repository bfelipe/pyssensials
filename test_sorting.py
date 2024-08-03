import unittest

import sorting


class SortingTestCase(unittest.TestCase):

    def test_swap(self):
        test_data = [1, 2]
        expected = [2, 1]
        sorting._swap(test_data, 0, 1)
        assert test_data == expected

    def test_bubble_sort(self):
        test_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        sorting.bubble_sort(test_data)
        assert len(test_data) == len(expected)
        assert test_data == expected

    def test_selection_sort(self):
        test_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        sorting.selection_sort(test_data)
        assert len(test_data) == len(expected)
        assert test_data == expected

    def test_insertion_sort(self):
        test_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        sorting.insertion_sort(test_data)
        assert len(test_data) == len(expected)
        assert test_data == expected

    def test_shell_sort(self):
        test_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        sorting.shell_sort(test_data)
        assert len(test_data) == len(expected)
        assert test_data == expected

    def test_merge_sort(self):
        test_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        sorting.shell_sort(test_data)
        assert len(test_data) == len(expected)
        assert test_data == expected

    def test_quick_sort(self):
        test_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        sorting.shell_sort(test_data)
        assert len(test_data) == len(expected)
        assert test_data == expected

    def test_heap_sort(self):
        test_data = [12, 3, 11, 13, 6, 5, 7]
        excepted = [3, 5, 6, 7, 11, 12, 13]
        sorting.heap_sort(test_data)
        assert len(test_data) == len(excepted)
        assert test_data == excepted
