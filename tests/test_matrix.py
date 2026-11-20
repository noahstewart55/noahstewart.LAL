#python -m pytest tests/test_matrix.py -v
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

# ---------- leftovers from 1.1 / 1.2 ----------

def test_add_sub_neg():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    assert A + B == Matrix([[6, 8], [10, 12]])
    assert B - A == Matrix([[4, 4], [4, 4]])
    assert -A == Matrix([[-1, -2], [-3, -4]])

def test_elementwise_non_square():
    C = Matrix([[1, 2, 3], [4, 5, 6]])
    D = Matrix([[2, 2, 2], [3, 3, 3]])
    assert C * D == Matrix([[2, 4, 6], [12, 15, 18]])

def test_init_copies_data():
    raw = [[1, 2], [3, 4]]
    A = Matrix(raw)
    raw[0][0] = 99
    assert A[0, 0] == 1


# ---------- 1.3: apply ----------

def test_apply():
    A = Matrix([[1, -2], [3, -4]])
    assert A.apply(abs) == Matrix([[1, 2], [3, 4]])
    assert A.apply(lambda x: x * 10) == Matrix([[10, -20], [30, -40]])

def test_apply_does_not_change_original():
    A = Matrix([[1, -2], [3, -4]])
    A.apply(abs)
    assert A == Matrix([[1, -2], [3, -4]])


# ---------- 1.3: sum ----------

S = Matrix([[1, 2, 3],
            [4, 5, 6]])

def test_sum_all():
    assert S.sum() == 21

def test_sum_axis0():
    result = S.sum(axis=0)
    assert result == Matrix([[5, 7, 9]])
    assert result.shape == (1, 3)

def test_sum_axis1():
    result = S.sum(axis=1)
    assert result == Matrix([[6], [15]])
    assert result.shape == (2, 1)


# ---------- 1.3: indexing ----------

def test_getitem():
    A = Matrix([[1, 2], [3, 4]])
    assert A[0, 1] == 2
    assert A[1, 0] == 3
    assert A[-1, -1] == 4

def test_setitem():
    A = Matrix([[1, 2], [3, 4]])
    A[1, 0] = 99
    assert A == Matrix([[1, 2], [99, 4]])

def test_getitem_out_of_range():
    A = Matrix([[1, 2], [3, 4]])
    with pytest.raises(IndexError):
        A[5, 0]


# ---------- 1.3: random ----------

def test_random_shape_and_type():
    R = Matrix.random(3, 4, 0.5)
    assert isinstance(R, Matrix)
    assert R.shape == (3, 4)

def test_random_in_range():
    R = Matrix.random(10, 10, 0.5)
    for i in range(R.rows):
        for j in range(R.cols):
            assert -0.5 <= R[i, j] <= 0.5

def test_random_differs():
    assert Matrix.random(3, 3, 1) != Matrix.random(3, 3, 1)


# ---------- 1.3: add_row ----------

def test_add_row():
    A = Matrix([[1, 2], [3, 4]])
    b = Matrix([[10, 20]])
    assert A.add_row(b) == Matrix([[11, 22], [13, 24]])

def test_add_row_does_not_change_original():
    A = Matrix([[1, 2], [3, 4]])
    A.add_row(Matrix([[10, 20]]))
    assert A == Matrix([[1, 2], [3, 4]])

def test_add_row_shape_mismatch():
    A = Matrix([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        A.add_row(Matrix([[1, 2, 3]]))