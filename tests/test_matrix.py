import pytest
from src.linalg.matrix import Matrix

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

def test_shape():
    assert A.shape == (2, 2)

def test_matmul():
    assert A @ B == Matrix([[19, 22], [43, 50]])

def test_elementwise_mul():
    assert A * B == Matrix([[5, 12], [21, 32]])

def test_scalar_mul_both_sides():
    assert 2 * A == A * 2 == Matrix([[2, 4], [6, 8]])

def test_associative():
    assert (A @ B) @ A == A @ (B @ A)

def test_transpose_twice():
    assert A.T.T == A

def test_non_square_matmul():
    C = Matrix([[1, 2, 3]])        # 1×3
    D = Matrix([[1], [2], [3]])    # 3×1
    assert C @ D == Matrix([[14]])

def test_shape_mismatch_raises():
    with pytest.raises(ValueError):
        A @ Matrix([[1, 2, 3]])
#python -m pytest tests/test_matrix.py -v