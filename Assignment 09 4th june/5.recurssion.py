'''5. Run a program to demonstrate Fibonacci and Factorial through recursion'''


def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
n=int(input("no of terms:"))
if n <=0:
    print("positive no")
else:
    print("fibonacci")
for i in range(n):
    print(fibonacci(i))



'''
#factorial

def factorial(n):  
   if(n == 1):  
       return n  
   else:  
       return n*factorial(n-1)    
num = int(input("Enter a number: "))    
if(num < 0):  
   print("Factorial not found for negative numbers")  
elif(num == 0):  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,factorial(num))
'''
