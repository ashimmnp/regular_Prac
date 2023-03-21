import numpy as np
print("Enter the values for the 3x3 matrix in order to find out the inverse.:)")
mat1 =[ ]
for i in range (3):
    row1 =[ ]
    for j in range(3):
        ele1=int(input("Enter the value for {:d} {:d}: ".format(i+1,j+1)))
        row1.append(ele1)
    mat1.append(row1)
print("Matrix'A': ",mat1)
mat=np.array(mat1)
print("Your Matrix is:")
print(mat)
#an=[ ]#ans=np.array(an)#ans=1/6 * mat#print(ans)#print(mat[1,0])#Finding out the determinant...
tri = mat[0,0]*(mat[1,1]*mat[2,2]-mat[1,2]*mat[2,1])-mat[0,1]*(mat[1,0]*mat[2,2]-mat[1,2]*mat[2,0])+mat[0,2]*(mat[1,0]*mat[2,1]-mat[1,1]*mat[2,0])
cof0=[ ]
cof1=[]
cof2=[]
ad=[ ]
cof0.append((mat[1,1]*mat[2,2]-mat[1,2]*mat[2,1]))
cof0.append(-(mat[0,1]*mat[2,2]-mat[0,2]*mat[2,1]))
cof0.append((mat[0,1]*mat[1,2]-mat[0,2]*mat[1,1]))
ad.append(cof0)
cof1.append(-(mat[2,2]*mat[1,0]-mat[2,0]*mat[1,2]))
cof1.append((mat[0,0]*mat[2,2]-mat[0,2]*mat[2,0]))
cof1.append(-(mat[0,0]*mat[1,2]-mat[1,0]*mat[0,2]))
ad.append(cof1)
cof2.append((mat[1,0]*mat[2,1]-mat[1,1]*mat[2,0]))
cof2.append(-(mat[0,0]*mat[2,1]-mat[0,1]*mat[2,0]))
cof2.append((mat[0,0]*mat[1,1]-mat[0,1]*mat[1,0]))
ad.append(cof2)
#cof10= -mat[1,0]*(mat)3
#adj.append(cof)
print("Determinant is:")
print(tri)
print("Adjoint is:")
adj = np.array(ad)
print(adj)
inverse=[]
inv=np.array(inverse)
print("Inverse is:")
inv = 1/tri *adj
print(inv)