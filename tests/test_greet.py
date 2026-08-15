import sys
import os

# Add src to path so we can import greet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lib.greet import greet


def test_greet_with_a():
    """greet('a')가 'Hi a'를 돌려준다"""
    assert greet('a') == 'Hi a'


def test_greet_with_b():
    """greet('b')가 'Hi b'를 돌려준다"""
    assert greet('b') == 'Hi b'
