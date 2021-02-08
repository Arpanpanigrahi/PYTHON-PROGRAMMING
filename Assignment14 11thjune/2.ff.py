import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def circumference(self):
        return 2*math.pi*self.radius
    def diameter(self):
        return 2*self.radius
    def  distance(x1,y1,x2,y2,self):
        dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
        return dist
   
    
 
r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:",round(obj.area()))
print("Perimeter of circle:",round(obj.circumference()))
print("Diameter of circle:",round(obj.diameter()))
print("Distance:",round(obj.distance(x1,y1,x2,y2)))

