'''1. Write functions to do following:
Take 3 sides of triangle as input and do following:
i. Return True for a valid triangle sides else false
ii. Classify the triangle as "Equilateral", "Rightangled", "Isosceles", "Scalene" (Default).
iii. Provided the given sides are valid else return NotValid
iv. Provided the triangle is "valid" and "Right angled" return the radius of circumcenter else return -1
'''

def istriangle(a,b,c):
    if((a+b)>c and (b+c)>a and (c+a)>b):
       return 1
    else:
        return -1
    
def triangletype(a,b,c):
    if (a==b and b==c):
        return "equilateral"
    elif (a**2+b**2==c**2):
        return "rightangled"
    elif (a==b or b==c or c==a):
        return "Isosceles"
    else:
        return "Scalene"


print("Enter the lengths of side of the triangle")
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

if (istriangle(a,b,c)==1):
    print("True")
else:
    print("False")
if(istriangle(a,b,c)==1):
    print(triangletype(a,b,c))
if(istriangle(a,b,c)==1):
    print("valid")

