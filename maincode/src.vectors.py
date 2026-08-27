### first function -- vector addition function

def add(v,w):
    u = [0,0]
    b = v[0] + w[0]
    c = v[1] + w[1]

    u = [b,c]
    return u

## test -- returns the value of the function
a=[2,4]
b=[24,2]
c = add(a,b)
print(c)
