import unittest

from src.alembic_api import sum_int


class TestFunctions(unittest.TestCase):
    def test_sum_int_returns_expected_result(self):
        self.assertEqual(2, sum_int(1, 1))
