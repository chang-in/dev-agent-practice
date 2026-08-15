from src.lib.greet import greet


def test_greet_with_a():
    """greet('a')가 'hello a'를 돌려준다"""
    assert greet('a') == 'hello a'
