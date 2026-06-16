#For area of trapezium we need both sides length and height of that trapezium
#Area of trapezium = 1/2*(a+b)*height
#Defining function
def areaoftrapezium(a, b, height):
	area = 1/2*(a+b)*height
	return area

#Taking inputs from the user
a = int(input("Enter the length of first side: "))
b = int(input("Enter the length of second side: "))
height = int(input("Enter the height: "))
area = areaoftrapezium(a, b, height)
print(f"The area of trapezium is {area}")
