from src.lib.goodbye import goodbye


def test_goodbye_with_name():
    assert goodbye('b') == 'goodbye b'
