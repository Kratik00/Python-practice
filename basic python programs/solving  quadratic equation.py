#For solving a quadratic equation we need three inputs a, b and c. 
# We can use Dharacharya's formula to find the roots of the equation. The formula is:
# x = (-b ± √(b² - 4ac)) / 2a 
import math
#defining a function  to solve quadratic equation
def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d))/(2*a)
        root2 = (-b - math.sqrt(d))/(2*a)
    elif d == 0:
        root1 = -b/(2*a)
        root2 = root1
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(-d)/(2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
    return root1, root2

#Taking input from user
try:
    a = int(input("Enter the coefficient of x^2: "))
    b = int(input("Enter the coefficient of x: "))
    c = int(input("Enter the constant value: "))
    root1, root2 = solve_quadratic(a, b, c)
    print(f"The root of {a}x^2 + {b}x + {c} is {root1} and {root2}")
except ValueError:
    print("Enter the valid integer.")