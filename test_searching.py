import unittest

import searching


class SearchingTestCase(unittest.TestCase):

    def test_linear(self):

        test_data = [1, 4, 7, 8, 2]

        result = searching.unordered_linear(2, test_data)
        assert result is True

        result = searching.ordered_linear(2, test_data)
        assert result is False

        result = searching.ordered_linear(7, test_data)
        assert result is True

        result = searching.unordered_linear(7, test_data)
        assert result is True

        result = searching.unordered_linear(3, test_data)
        assert result is False

        result = searching.ordered_linear(3, test_data)
        assert result is False

    def test_binary(self):

        test_data = [1, 2, 4, 7, 8]

        result = searching.binary(2, test_data)
        assert result is True

        result = searching.binary(7, test_data)
        assert result is True

        result = searching.binary(3, test_data)
        assert result is False
