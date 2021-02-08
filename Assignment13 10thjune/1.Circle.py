 #1. Given attributes (x,y,r) for two circles identify if the circles "intersect",
#"touch" or "Not intersect  
  
def circle(x1, y1, x2, y2, r1, r2): 
	distance = (x1 - x2)*(x1 - x2)+(y1 - y2)*(y1 - y2); 
	radius =(r1 + r2); 
	if (distance==radius): 
		return 1
	elif (distance > radius): 
		return -1
	else: 
		return 0	    
x1=10
y1=40
x2=3
y2=89
r1=2
r2=8
z= circle(x1, y1, x2, y2, r1, r2) 
if (z == 1): 
	print("Circle touch each other.") 
elif (z < 0): 
	print("Circle not intersect each other.") 
else: 
	print("Circle intersect each other.") 






















'''

Distance between centers C1 and C2 is calculated as
 C1C2 = sqrt((x1 - x2)2 + (y1 - y2)2).
There are three condition arises.
1. If C1C2 == R1 + R2
     Circle A and B are touch to each other.
2. If C1C2 > R1 + R2
     Circle A and B are not touch to each other.
3. If C1C2 < R1 + R2
      Circle intersects each other.
'''
