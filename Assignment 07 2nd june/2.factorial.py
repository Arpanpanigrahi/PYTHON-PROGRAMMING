'''2. Write a program to take integral numbers and calculate the factorial.
Note: If factorial is not defined return -1
'''

def fact(n):
    if n == 1 or n==0:
        return 1
    elif n < 0:
        return -1
    else:
        return n*fact(n-1)
num = input("Enter a Number:")
print(fact(int(num)))



'''
#Alternate01

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)
num = int(input("Enter a Number:"))
if num < 0:
    print("Factorial cannot be found for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is:",factorial(num))
'''

'''
#Alternate02

num = int(input("enter a number:"))
fac = 1
for i in range(1,num+1):
    fac = fac * i
print("factorial of",num," is",fac)

'''
