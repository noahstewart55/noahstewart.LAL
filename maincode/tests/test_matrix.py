from maincode.vectorfunctions import shape
from maincode.vectorfunctions import matmul
from maincode.vectorfunctions import norm
import pytest

import pytest

def test_matmul_dimension_mismatch():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError):
        matmul(A, B)
@pytest.mark.parametrize("A, B, expected", [
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
    ([[2]], [[3]], [[6]]),
    ([[1, 2, 3]], [[1], [2], [3]], [[14]]),
])
def test_matmul_cases(A, B, expected):
    assert matmul(A, B) == expected
def test_norm():
    assert norm([3, 4]) == pytest.approx(5.0)