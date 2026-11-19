class Matrix:
    def __init__(self, datalist):
        self.data = datalist
        self.rows = len(datalist)
        self.cols = len(datalist[0])
    def __repr__(self):
        rows, cols = self.rows, self.cols
        for row in range(rows):
            print(f"{self.data[row]}")
   
A = Matrix([[1,2],[3,4]])
print(A)