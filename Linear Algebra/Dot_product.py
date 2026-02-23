import math
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

          
class vector:
     
    def __init__(self,vec):
        self.vec=np.array(vec)
   
    def add(self,vec1,vec2):
        r1=len(vec1)
        r2=len(vec2)
        if r1!=r2:
            print({"invalid vectors "})
            return 0
        tmp_vec=[]
        for i in range(r1):
            tmp_vec.append(vec1[i]+vec2[i])
        return tmp_vec

    def mul(self,vec1,vec2):
        r1=len(vec1)
        r2=len(vec2)
        if r1!=r2:
            print({"invalid vectors "})
            return 0
        tmp_vec=[]
        for i in range(r1):
            tmp_vec.append(vec1[i]*vec2[i])
        return tmp_vec
    def linear_comb(self,vec1,scale1,vec2,scale2):
            r1=len(vec1)
            r2=len(vec2)
            if r1!=r2:
                print({"invalid vectors!!! "})
                return 0
            tmp_vec=[]
            for i in range(r1-1):
                tmp_vec.append((scale1*vec1[i])+(scale2*vec2[i]))
            return tmp_vec
        

    def vector_norm(self,vec1):
        tmp=0
        for i in range(len(vec1)):
            tmp+=vec1[i]**2
        return tmp**1/2
    
    def angle(self,vec1,vec2):
        tmp=0
        dot=0
        real=0
        
        dot=sum(vec1[i] * vec2[i] for i in range(len(vec1)))
        norm1 = self.vector_norm(vec1)
        norm2 = self.vector_norm(vec2)
        return math.acos(dot / (norm1 * norm2))

    
    def check_ort(self,vec1,vec2):
        if sum(self.mul(vec1,vec2))==0:
            print("orthangualy vector")
            return True
        return False
    
        

        
                

        
