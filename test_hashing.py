import unittest

import hashing

class HashingTestCase(unittest.TestCase):

    def test_reminder_hash(self):
        test_data = 12345
        table_size = 11
        result = hashing.reminder_hash(test_data, table_size)
        assert result == 3

    def test_folding_hash(self):
        test_data = 12345
        table_size = 11
        result = hashing.folding_hash(test_data, table_size)
        assert result == 8

    def test_revered_folding_hash(self):
        test_data = 12345
        table_size = 11
        result = hashing.reversed_folding_hash(test_data, table_size)
        assert result == 1

    def test_mid_square_hash(self):
        test_data = 12345
        table_size = 11
        result = hashing.mid_square_hash(test_data, table_size)
        assert result == 6
