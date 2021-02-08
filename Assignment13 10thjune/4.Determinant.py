#4. Take a 2X2 square matrix as input and calculate the determinant:
#    Input -
#    [[1,2],[3,4]]
#    Output - (-2)


m=[[1,2],[3,4]]
print("Matrix:")
for array in m:
    print(array)
det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
print("Determinant of matrix is:",det)
