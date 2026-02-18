import numpy as np
a=np.array([[1,2],
              [3,4]])
b=np.array([[5,6],
            [7,8]])

c=np.array([[0,0],
            [0,0]
             ])

def row(num,matrix):
    
    return matrix[num-1,:]

def col(num,matrix):
    return matrix[:,num-1]


def dot(matrix1,matrix2,r,c):
    tmp=0
    rov_v=row(r,matrix1)
    col_v=col(c,matrix2)
    for i in range(len(rov_v)):
        tmp+=rov_v[i]*col_v[i]
    return tmp    

def dot_matrix(matrix1,matrix2,target):
    rows1,cols1=matrix1.shape
    rows2,cols2=matrix2.shape 
    if cols1!=rows2:
        print("invalid matrix to product!!")
        return 0 
    for i in range(rows1):
        for j in range(cols2):
            target[i][j]=dot(matrix1,matrix2,i+1,j+1)
    return target

          
print(dot_matrix(a,b,c))         
print(a@b)
