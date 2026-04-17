# For calculating the area and volume of a sphere we need to know the radius of the sphere. The formula for calculating the area of a sphere is: Area = 4 * pi * radius * radius and the formula for calculating the volume of a sphere is: Volume = (4/3) * pi * radius * radius * radius.
# Here is a simple Python program to calculate the area and volume of a sphere:
# Function to calculate the area of a sphere
import math as m

def area_of_sphere(radius):
    area = 4*m.pi*radius*radius
    return area

#Function to calculate the volume of a sphere 
def volume_of_sphere(radius):
    volume = (4/3)*m.pi*radius*radius*radius
    return volume

#Get user input for radius 
try: 
    radius =  float(input("Enter the radius of the sphere : "))

    area = area_of_sphere(radius)
    volume = volume_of_sphere(radius)

    print(f"The area of the sphere is: {area}")
    print(f"The volume of the sphere is: {volume}")
except ValueError:
    print("Please enter valid radius for the sphere.")

