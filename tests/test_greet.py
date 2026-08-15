import unittest
from src.lib.greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_hello_with_name(self):
        """greet('a')가 'hello a'를 돌려준다"""
        self.assertEqual(greet('a'), 'hello a')


if __name__ == '__main__':
    unittest.main()
