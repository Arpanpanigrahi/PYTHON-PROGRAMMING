'''
3. Write a program that takes two matrices as input and does matrix multiplication (Naive approach)
Hint - use 3 nested loops
Example:
Input
Take a 3x3 matrix
A = [[12, 7, 3],
[ 4, 5, 6],
[ 7, 8, 9]]
Take a 3x4 matrix
B = [[5, 8, 1, 2],
[6, 7, 3, 0],
[4, 5, 9, 1]]
Output
[114, 160, 60, 27]
[ 74, 97, 73, 14]
[119, 157, 112, 23]
'''

m=[]
for i in range(3):
        a=[]
        for j in range(3):
                j=int(input("Enter Number ["+str(i)+"] ["+str(j)+"]"))
                a.append(j)
        m.append(a)
n=[]
for i in range(3):
        b=[]
        for j in range(3):
                j=int(input("Enter Number ["+str(i)+"] ["+str(j)+"]"))
                b.append(j)
        n.append(a)
print("First Matrix is...")
for i in range(3):
        for j in range(3):
                print(m[i][j],end=" ")
        print()
print("Second Matrix is...")
for i in range(3):
        for j in range(3):
                print(n[i][j],end=" ")
        print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
        for j in range(3):
                for k in range(3):
                        result[i][j]= result[i][j]+m[i][k]*n[k][j]
print("Multiplication of two matrix is...")
for i in range(3):
        for j in range(3):
                print(result[i][j],end=" ")
        print()
                


'''
#Alternate Method

A = [[12, 7, 3], 
     [4, 5, 6], 
     [7, 8, 9]] 

B = [[5, 8, 1, 2], 
     [6, 7, 3, 0], 
     [4, 5, 9, 1]] 
	
result = [[0, 0, 0, 0], 
	  [0, 0, 0, 0], 
	  [0, 0, 0, 0]] 

for i in range(len(A)):
	for j in range(len(B[0])):  
		for k in range(len(B)): 
			result[i][j] =result[i][j] + A[i][k] * B[k][j] 
for r in result: 
	print(r) 
'''
