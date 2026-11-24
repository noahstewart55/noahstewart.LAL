from src.autograd.value import Value

def test_forward():
    a = Value(2.0); b = Value(-3.0)
    c = a * b + 1
    assert c.data == -5.0

def test_records_parents():
    a = Value(2.0); b = Value(3.0)
    c = a + b
    assert c._prev == {a, b}
    assert c._op == '+'

def test_accepts_numbers():
    a = Value(2.0)
    assert (a + 1).data == 3.0
    assert (a * 4).data == 8.0

def test_grad_starts_at_zero():
    assert Value(5.0).grad == 0.0
def test_backward_example():
    a = Value(2.0); b = Value(-3.0); c = Value(10.0); d = Value(-2.0)
    L = (a * b + c) * d
    L._backward()
    assert (a.grad, b.grad, c.grad, d.grad) == (6.0, -4.0, -2.0, 4.0)

def test_reused_value():
    a = Value(3.0)
    b = a + a
    b._backward()
    assert a.grad == 2.0     # fails if you used = instead of +=

def test_reused_in_product():
    a = Value(3.0)
    b = a * a                # b = a², so db/da = 2a = 6
    b._backward()
    assert a.grad == 6.0
