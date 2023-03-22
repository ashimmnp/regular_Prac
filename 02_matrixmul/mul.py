import numpy as np
print("Enter the elemenmts for the first matrix->")
matx=[ ]
maty=[ ]
for i in range(3):
  rowx=[ ]
  for j in range(3):
    rowx.append(int(input("Enter the value for A->{:d} {:d}: ".format(i+1,j+1))))
  matx.append(rowx)
print()
print("Enter the elements for the Second matrix->")
for i in range(3):
  rowy=[ ]
  for j in range(3):
    rowy.append(int(input("Enter the value for B->{:d} {:d}: ".format(i+1,j+1))))
  maty.append(rowy)
print()
matA=np.array(matx)
matB=np.array(maty)
mult=[ ]
row1=[ ]
row1.append((matA[0,0]*matB[0,0])+(matA[0,1]*matB[1,0])+(matA[0,2]*matB[2,0]))
row1.append((matA[0,0]*matB[0,1])+(matA[0,1]*matB[1,1])+(matA[0,2]*matB[2,1]))
row1.append((matA[0,0]*matB[0,2])+(matA[0,1]*matB[1,2])+(matA[0,2]*matB[2,2]))
mult.append(row1)
row2=[ ]
row2.append((matA[1,0]*matB[0,0])+(matA[1,1]*matB[1,0])+(matA[1,2]*matB[2,0]))
row2.append((matA[1,0]*matB[0,1])+(matA[1,1]*matB[1,1])+(matA[1,2]*matB[2,1]))
row2.append((matA[1,0]*matB[0,2])+(matA[1,1]*matB[1,2])+(matA[1,2]*matB[2,2]))
mult.append(row2)
row3=[]
row3.append((matA[2,0]*matB[0,0])+(matA[2,1]*matB[1,0])+(matA[2,2]*matB[2,0]))
row3.append((matA[2,0]*matB[0,1])+(matA[2,1]*matB[1,1])+(matA[2,2]*matB[2,1]))
row3.append((matA[2,0]*matB[0,2])+(matA[2,1]*matB[1,2])+(matA[2,2]*matB[2,2]))
mult.append(row3)
res=np.array(mult)
print("Matrix Set A:")
print(matA)
print("Matrix Set B: ")
print(matB)
print("Multiplied AxB is:")
print(res)
