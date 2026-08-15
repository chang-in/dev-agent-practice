import unittest
from src.lib.greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name_a(self):
        """greet('a')가 'hello a'를 돌려준다 (P-1 acceptanceCriteria)"""
        self.assertEqual(greet('a'), 'hello a')


if __name__ == '__main__':
    unittest.main()
