#Ejercicio_003
A=((1,2,3),(4,5,6))
B=((-1,0),(0,1),(1,1))
# print(tuple(tuple(elem_1 * elem_2 for elem_1, elem_2 in zip(A,B))\
#       for A,B in zip(A, B)))
C=[[0,0],
   [0,0],]

# iterate through rows of X
for i in range(len(A)):
   # iterate through columns of Y
   for j in range(len(B[0])):
       # iterate through rows of Y
       for k in range(len(B)):
           C[i][j] += A[i][k] * B[k][j]
for result in C:
    print(tuple(result))