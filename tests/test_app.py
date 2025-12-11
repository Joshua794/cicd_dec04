import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_add2():
    assert add(5, 6) == add(6, 5)

def test_sub():
    assert sub(10, 6) == 4

def test_sub2():
    assert sub(10, 6) != 3

def test_sub3():
    assert sub(10, 6) == -1 * sub(6, 10)
