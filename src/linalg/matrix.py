import math
import random
class Matrix:
    #write __eq__ at some point
    def __init__(self, datalist):
        self.data = [row.copy() for row in datalist]
        self.rows = len(datalist)
        self.cols = len(datalist[0])
    def __repr__(self):
        data=self.data
        return "\n".join(str(row) for row in self.data)
    def __eq__(self,other):
        if not isinstance(self,Matrix) or not isinstance(other,Matrix):
            return NotImplemented
        mat1=self.data
        mat2=other.data
        provendifferent=False
        if self.shape==other.shape:
            try:
                for row in range(len(mat1)-1):
                    for col in range(len(mat1)-1):
                        if (mat1[row][col])==(mat2[row][col]):
                            continue
                        else:
                            provendifferent=True
                            break
                    if provendifferent==True:
                        return False
                        break
                    else:
                        continue
            except IndexError:
                return False
        else:
            return False

        return True
    @property
    def shape(self):
        shape = self.rows, self.cols
        return shape
    @property
    def T(self):
        t = []
        t_row = []
        current_col = 0
        i=0
        while True:
            if i > len(self.data) or current_col >= self.cols:
                break
            t_row.append(self.data[i][current_col])
            if i == len(self.data)-1:
                current_col +=1
                t.append(t_row)
                i=0
                t_row=[]
                continue
            i += 1
        return Matrix(t)       
    def __add__(a, b):
        c = []
        rowc=[]
        alist=a.shape
        blist=b.shape
        arows=alist[0]
        acols=alist[1]
        brows=blist[0]
        bcols=blist[1]
        if arows!=brows or acols!=bcols:
            raise ValueError("Matrices must have equal dimensions to add!")
        else:
            for row in range(arows):
                for col in range(acols):
                    rowc.append(a.data[row][col]+b.data[row][col])
                c.append(rowc)
                rowc=[]
        return Matrix(c)
    def __sub__(a, b):
        c = []
        rowc=[]
        alist=a.shape
        blist=b.shape
        arows=alist[0]
        acols=alist[1]
        brows=blist[0]
        bcols=blist[1]
        if arows!=brows or acols!=bcols:
            raise ValueError("Matrices must have equal dimensions to add!")
        else:
            for row in range(arows):
                for col in range(acols):
                    rowc.append(a.data[row][col]-b.data[row][col])
                c.append(rowc)
                rowc=[]
        return Matrix(c)
    def __matmul__(self,other):
            c=[]
            arows, acols = self.shape
            brows, bcols = other.shape
            ##first loop to create c[0][0]
            x=0
            y=0
            crow=[]
            product=0
            #c.append(crow)
            ##create a loop that loops this loop
            # through the first row of products and appends each to crow, then crow to c, then reset crow
            if acols==brows:
                for row in range(arows):
                    crow=[]
                    for col in range(bcols):
                        product=0
                        for itr in range(acols):
                            product += self.data[row][itr] * other.data[itr][col]
                        crow.append(product)
                    c.append(crow)
            else:
                raise ValueError("Dimension Mismatch")
            return Matrix(c)            


    def __rmul__(a,b):
        if isinstance(b,Matrix) and (isinstance(a,float) or isinstance(a,int)):
            n = []
            nrow=[]
            rows,cols = b.shape
            for row in range(rows):
                for col in range(cols):
                    nrow.append(a * b.data[row][col])
                n.append(nrow)
                nrow=[]
            return Matrix(n)
        
        elif isinstance(a,Matrix) and (isinstance(b,float) or isinstance(b,int)):
            n = []
            nrow=[]
            rows,cols = a.shape
            for row in range(rows):
                for col in range(cols):
                    nrow.append(b*a.data[row][col])
                n.append(nrow)
                nrow=[]
            return Matrix(n)        
        elif isinstance(b,Matrix) and isinstance(a,Matrix) and(a.shape==b.shape):
            mat1=a.data
            mat2=b.data
            arows,acols=a.shape
            brows,bcols=b.shape
            newmat=[]
            
            for row in range(brows):
                newrow=[]
                for col in range(acols):
                    newrow.append((mat1[row][col])*(mat2[row][col]))
                newmat.append(newrow)
            return Matrix(newmat)

    def __mul__(a,b):
        if isinstance(b,Matrix) and (isinstance(a,float) or isinstance(a,int)):
            n = []
            nrow=[]
            rows,cols = b.shape
            for row in range(rows):
                for col in range(cols):
                    nrow.append(a * b.data[row][col])
                n.append(nrow)
                nrow=[]
            return Matrix(n)
        
        elif isinstance(a,Matrix) and (isinstance(b,float) or isinstance(b,int)):
            n = []
            nrow=[]
            rows,cols = a.shape
            for row in range(rows):
                for col in range(cols):
                    nrow.append(b*a.data[row][col])
                n.append(nrow)
                nrow=[]
            return Matrix(n)
        elif isinstance(b,Matrix) and isinstance(a,Matrix) and(a.shape==b.shape):
            mat1=a.data
            mat2=b.data
            arows,acols=a.shape
            brows,bcols=b.shape
            newmat=[]
            for row in range(arows):
                newrow=[]
                for col in range(bcols):
                    newrow.append((mat1[row][col])*(mat2[row][col]))
                newmat.append(newrow)
            return Matrix(newmat)

    def zeros(r,c):
        rows=r
        cols=c
        rowlist=[]
        zeromat=[]
        for i in range(cols):
            rowlist.append(0)
        for j in range(rows):
            zeromat.append(rowlist)
        return Matrix(zeromat)
    def identity(l):
        mat=[]
        spot=0
        for j in range(l):
            rowlist=[]
            for i in range(l):
                if i==spot:
                    rowlist.append(1)
                else:
                    rowlist.append(0)
            mat.append(rowlist)
            spot+=1
        return Matrix(mat)
    def __neg__(self):
        mat=self.data
        negmat=[]
        
        for row in mat:
            negmatrow=[]
            for col in row:
                negmatrow.append(-col)
            negmat.append(negmatrow)
        return Matrix(negmat)
    ##1.3
    def apply(self,f): 
        mat0 = self.data
        mat1=[]
        rows, cols = self.shape
        for row in range(rows):
            newrow=[]
            for col in range(cols):
                newrow.append(f(mat0[row][col]))
            mat1.append(newrow)
        return Matrix(mat1)
    def sum(self,axis=None): 
        mat0 = self.data
        s=0
        list1=[]
        list2=[]
        rows, cols = self.shape
        if axis == None: #sum all entrys
            for row in mat0:
                s+=sum(row)
            return s
        elif axis==1: #sum across each row
            for row in mat0:
                list1.append([sum(row)])
            return Matrix(list1)
        elif axis==0: #sum down each column
            for i in range(cols):
                list1.append(0)
            for r in range(rows):
                for c in range(cols):
                    list1[c]= list1[c]+mat0[r][c]
            list2.append(list1)
            return Matrix(list2)
    def __getitem__(self,key):
        mat0 = self.data
        r,c = key
        val=mat0[r][c]
        return val        
    def __setitem__(self,key,value):
        mat0 = self.data
        r,c = key
        mat0[r][c]=value
    @classmethod
    def random(cls,r,c,scale):
        rmat=[]
        for row in range(r):
            newline=[]
            for j in range(c):
                newline.append(random.uniform(-scale,scale))
            rmat.append(newline)
        return Matrix(rmat)
    def add_row(self, b): #b is one line (list) added as the last row of the matrix
        a = self.data
        rows = self.rows
        cols = self.cols
        z = [[0]*cols for _ in range(rows)]
        if cols == b.cols:
            for row in range(rows):
                for col in range(cols):
                    z[row][col]=a[row][col]+b[0,col]
            return Matrix(z)
        else:
            raise ValueError(f"shape mismatch: matrix is {self.shape}, row is {b.shape}")