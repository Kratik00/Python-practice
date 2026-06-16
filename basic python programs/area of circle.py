#For finding area of any circle we just need radius of the Circle
#area of circle = pi*r*r
import math 
def area_of_circle(r):
	area = math.pi*r*r
	return area
 #taking inputs from user
r = int(input("Enter radius: "))
area = area_of_circle(r)
print(f"The area of circle is {area}")
