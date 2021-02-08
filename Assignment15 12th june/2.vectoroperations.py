#2. Design a vector class that will support some of the vector operations like:
#− Add (+)
#− Sub (-)
#− Mul (*)
#− ABS (abs)
#Example:
#v1=Vector(3,2)
#v2=Vector(2,3)
#v3=v1+v2
#Output
#v3 => Vector(5,5)

import math
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return ("Vector({},{})".format(self.x,self.y))

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x,y)

    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x,y)

    def __abs__(self):
        return math.hypot(self.x,self.y)

###Execution###
v1 = Vector(1,2)
v2 = Vector(4,5)
print(v1+v2)
print(v1-v2)
print(v1*v2)
print(abs(v1))
print(type(v1))

