'''4. Run below code that will generate a matrix as an input and print all the even numbers in it import random
mat = [[random.randint(1,10) for i in range(4)] for row in range(4)]
print(mat)
'''

import random
mat = [[random.randint(1,10) for i in range(4)] for j in range(4)]
print(mat)
print("Even elements")
for i in mat:
    for j in i:
      if j%2 == 0:
        print(j,end=" ")
