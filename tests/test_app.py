import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div, log, square, sin, cos, sqrt, percentage

# ---BASIC FUNCTIONS--- #
# ---ADD--- #
def test_add():
    assert add(5, 6) == 11
def test_add2():
    assert add(5, 6) != 10
def test_add3():
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

# ---ADVANCED FUNCTIONS--- #
# ---LOG--- #
def test_log():
    assert log(100, 10) == 2
def test_log2():
    assert log(8, 2) == 3
def test_log3():
    assert round(log(math.e, math.e), 10) == round(1, 10)

# ---SQUARE--- #
def test_square():
    assert square(5) == 25
def test_square2():
    assert square(10) == 100
def test_square3():
    assert square(5) == mult(5, 5)

# ---SIN--- #
def test_sin():
    assert round(sin(0), 10) == 0
def test_sin2():
    assert round(sin(math.pi / 2), 10) == 1
def test_sin3():
    assert round(sin(math.pi), 10) == 0 

# ---COS--- #
def test_cos():
    assert round(cos(0), 10) == 1
def test_cos2():
    assert round(cos(math.pi / 2), 10) == 0
def test_cos3():
    assert round(cos(math.pi), 10) == -1

# ---SQRT--- #
def test_sqrt():
    assert sqrt(16) == 4
def test_sqrt2():
    assert sqrt(25) == 5
def test_sqrt3():
    assert sqrt(square(7)) == 7

# ---PERCENTAGE--- #
def test_percentage():
    assert percentage(25, 100) == 25
def test_percentage2():
    assert percentage(50, 200) == 25
def test_percentage3():
    assert percentage(3, 4) == 75
