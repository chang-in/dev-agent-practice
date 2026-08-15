import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.lib.greet import greet


def test_greet_with_name():
    """greet('a')가 'hello a'를 돌려준다"""
    assert greet('a') == 'hello a'
