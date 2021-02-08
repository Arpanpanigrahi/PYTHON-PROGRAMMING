'''3. Implement the circle problem using object oriented approach:
a. Create a circle class
b. Take center coordinates and radius as attributes
c. Define all related functions within the class like
i. Area
ii. Perimeter
iii. Center distance from origin
iv. Circumference distance from origin
d. Handle any exceptions and Not valid scenarios
'''

class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.142*self.radius*self.radius

    def perimeter(self):
        return 2*3.142*self.radius

NewCircle = Circle(8)
print("AREA:", NewCircle.area())
print("PERIMETER:", NewCircle.perimeter())




