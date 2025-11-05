
from src.main import get_basic

def test_basic():
    assert 1 == 1

def test_basic_2():
    assert get_basic() == 1
    assert get_basic() == 1