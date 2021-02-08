''' 5.Run a program to demonstrate Fibonacci and Factorial through recursion'''

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n= int(input("Enter number of terms:"))
if(n <= 0):
    print("Please enter positive integer")
else:
    print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))


'''
def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)
num=int(input("Enter a number:"))
if(num<0):
    print("Factorial not found for negative numbers")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    print("Factorial of",num,factorial(num))
'''
