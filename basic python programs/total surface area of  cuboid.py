#For calculating total surface area of cuboid we need three inputs length, breadth and height. The formula for calculating total surface area of cuboid is 2*(l*b + b*h + h*l)
#defining a function to calculate total surface area of cuboid
def surface_area_of_cuboid(l, b, h):
    area = 2 * (l*b + b*h + h*l)
    return area

#Taking input from user
try:
    length = float(input("Enter the length of cuboid: "))
    breadth = float(input("Enter the breadth of cuboid: "))
    height = float(input("Enter the height of cuboid: "))
    area = surface_area_of_cuboid(length, breadth, height)
    print(f"The total surface area of the cuboid is {area}")
except ValueError:
    print("Please enter valid input. It should be a number.")