# For finding the area of a regular polygon we need to know the number of sides and the length of each side. The formula for calculating the area of a regular polygon is: Area = (n * s^2) / (4 * tan(pi/n)) where n is the number of sides and s is the length of each side.
# Here is a simple Python program to calculate the area of a regular polygon:

import math as m

# Function to calculate the area of a regular polygon
def area_of_regular_polygon(sides, length):
    area = (sides * length * length) / (4 * m.tan(m.pi/sides))
    return area

# Get user input for number of sides and length of each side
try:
    sides  = int(input("Enter the number of sides of the regular polygon: "))
    length = float(input("Enter the length of each side of the regular polygon: "))
    area = area_of_regular_polygon(sides, length)
    print(f"The area of the regular polygon is: {area}")
except ValueError:
    print("Please enter valid number for both sides and length.")