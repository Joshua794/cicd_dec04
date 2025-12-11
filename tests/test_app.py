import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div

# ---ADD--- #
def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_add2():
    assert add(5, 6) == add(6, 5)

# ---SUB--- #
def test_sub():
    assert sub(10, 6) == 4

def test_sub2():
    assert sub(10, 6) != 3

def test_sub3():
    assert sub(10, 6) == (-1 * sub(6, 10))

# ---MULT--- #
def test_mult():
    assert mult(7, 8) == 56

def test_mult2():
    assert mult(7, 8) != 57

def test_mult3():
    assert mult(7, 8) == mult(8, 7)

# ---DIV--- #
def test_div():
    assert div(16, 8) == 2

def test_div2():
    assert div(mult(16, 8), 8) == 16

def test_div3():
    assert div(16, 8) == mult(16, div(1, 8))
