import sys
import os

# Add src to path so we can import greet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lib.greet import greet


def test_greet_with_a():
    """greet('a')가 'hello a'를 돌려준다"""
    assert greet('a') == 'hello a'
