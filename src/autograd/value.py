class Value:
    def __init__(self,data,_children=(), _op="", label=""):
        self.data = data
        self.grad = 0.0
        self._backward=lambda:None
        self._prev=set(_children)
        self._op = _op
        self.label=label
    def __repr__(self):
        return f"Value[data={self.data}]"
    def __add__(self, other):
        if not isinstance(other,Value):
            other = Value(other)
        if not isinstance(self,Value):
                    self = Value(self)
        out = Value(self.data + other.data, (self, other),'+')
        
        def _backward():
            self.grad =1.0 * out.grad
            other.grad = 1.0 * out.grad
        out._backward = _backward()
        return out
        
        
    def __mul__(self,other):
        if not isinstance(self,Value):
                    self = Value(self)
        if not isinstance(other,Value):
            other = Value(other)
        out = Value(self.data*other.data, (self, other),'*')
        def _backward():
            self.grad=other.grad*out.grad
            other.grad=self.grad*out.grad
        out._backward = _backward()
        return out

    def tanh(self):
        x=self.data
        t = (math.exp(2*x)-1)/(math.exp(2*x)+1)
        out= Value(t, (self, ), 'tanh')
        def _backward():
            self.grad = (1-t**2) * out.grad
        out._backward = _backward()
        return out

if __name__ == "__main__":
    a=Value(2.0)
    b=Value(-3.0)
    c=Value(10.0)
    d=Value(-2.0)
    L = (a*b + c) * d
    print(L._backward())