import sys
import os
import unittest

# Add src to path so we can import greet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lib.greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_a(self):
        """greet('a')가 'Hi a'를 돌려준다"""
        self.assertEqual(greet('a'), 'Hi a')

    def test_greet_with_b(self):
        """greet('b')가 'Hi b'를 돌려준다"""
        self.assertEqual(greet('b'), 'Hi b')


if __name__ == '__main__':
    unittest.main()
