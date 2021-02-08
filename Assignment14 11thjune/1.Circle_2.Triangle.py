'''
1. Implement circle class:
Create a circle class
• Declare and define an __init__ function that takes 3 parameters.
• Keep read and write access on the parameters private so that it can’t be changed directly from calling environment.
• Define all the methods of the circle.
• Make the class backward compatible so that access/update of parameters is possible directly and also through getter/setter function calls, but validation happens in all the cases
'''

class circle:
    def __init__(self,x=0,y=0,r=0):
        self.__x=x
        self.__y=y
        self.r=r
        
    @property
    def r(self):
       return self.__r
    @r.setter
    def r(self,r):
       print("After Authorization")
       assert r>0,"Value Error:Please enter a valid radius"
       self.__r=r
    def area(self):
        return 3.14*self__.r**2
    def circum(self):
        return 2*3.14*self__.r
    def center_dist(self):
        D=(self.__x**2+self.__y**2)**0.5
        return D
    def circum_dist(self):
       D=c1.center_dist()
       if D>self__.r:
          return D-self.__r
       else:
          return self.__r-D
x,y,r=input("Enter the coordinates and radius of the circle separated by space: ").split()
c1=circle(float(x),float(y),float(r))
print("Area :",c1.area())
print("Circumference:",c1.circum())
print("Distance from center to origin:",c1.center_dist())
print("Distance:",c1.circum_dist())
print(c1.x)

'''
#2. Similarly, create a triangle class

import math
a = int(input("Please enter the first side of a triangle  : "))
b = int(input("Please enter the second side of a triangle : "))
c = int(input("Please enter the third side of a triangle  : "))
class triangle():
   def __init__(self,a,b,c):
       self.a = a
       self.b = b
       self.c = c
   def area(self):
       s=(a + b + c)/2
       area=math.sqrt(s*(s-a)*(s-b)*(s-c))
       return area
   def perimeter(self): 
       perimeter=a + b + c
       return perimeter
t = triangle(a, b, c)
print("Area of a triangle:",t.area())
print("Perimeter of a triangle:",t.perimeter())

'''
