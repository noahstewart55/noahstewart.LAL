### first function -- vector addition function

def add(v,w):
    u = [0,0]
    b = v[0] + w[0]
    c = v[1] + w[1]

    u = [b,c]
    return u

## test -- returns the value of the function
## sept 20

def scale(c,v):
   scaled = [x*c for x in v]
   return scaled
#where w,v are lists
def dot(w,v):
    product=0
    ##theory comma w,v in list argument
    dotted = [wval*vval for wval,vval in zip(w,v)]
    ##product
    for n in dotted:
        product +=n

    return product
def magnitude(v):
    squarelist = [n**2 for n in v]
    presum=0
    for i in range(len(squarelist)):
        presum+=squarelist[i]
    return presum**(1/2)
### nested lists as matrices
#let matrix a be a nested list matrix

### write these functions
#shape(A) → (rows, cols)
#transpose(A)
#add(A, B)
#scale(c, A)
#pretty_print(A)
def shape(a):
    rows = len(a)
    cols = len(a[0])
    shape = rows, cols
    return shape

#sept 21 finsihing transpose -- working on..
def transpose(a):
    #shape within
    rows = len(a)
    cols = len(a[0])
    shape = rows, cols
    #create transposed matrix t
    t = []
    t_row = []
    current_col = 0
    i=0
    while True:
        if i > len(a) or current_col >= cols:
            break
        t_row.append(a[i][current_col])
        if i == len(a)-1:
            current_col +=1
            t.append(t_row)
            i=0
            t_row=[]
            continue
        i += 1
    return t
def add(a, b):
    c = []
    rowc=[]
    arows,acols = shape(a)
    brows,bcols = shape(b)
    if arows!=brows or acols!=bcols:
        raise ValueError("Matrices must have equal dimensions to add!")
    else:
        for row in range(arows):
            for col in range(acols):
                rowc.append(a[row][col]+b[row][col])
            c.append(rowc)
            rowc=[]
    return c
a=[[1,2],
   [4,5],
   [7,8]]
b=[[10,9,8],
   [7,6,5]]
## let c be a constant scalar factor for the matrix a
def scale(c,a):
    n = []
    nrow=[]
    rows,cols = shape(a)
    for row in range(rows):
        for col in range(cols):
            nrow.append(c*a[row][col])
        n.append(nrow)
        nrow=[]
    return n
##function that prints matrix from list form into legible matrix form
def matprint(a):
    rows,cols = shape(a)
    for row in range(rows):
        print(f"{a[row]}")


### watched matrix mult video
### going to implement new functions -- sept 21 1pm
### create first matmul iteration matmul = a*b
def matmul(a,b):
    c=[]

    arows, acols = shape(a)
    brows, bcols = shape(b)

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
                    product += a[row][itr] * b[itr][col]
                crow.append(product)
            c.append(crow)
    else:
        raise ValueError("Dimension Mismatch")
    return c

def norm(a):
    n=0
    for i in range(len(a)):
        n += a[i]**2
        c= n**(1/2)

    return c










