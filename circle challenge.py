import math as m

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return m.pi*(self.radius**2)

    def perimeter(self):
        return 2*m.pi*self.radius

r = circle(5)
print(r.area())
print(r.perimeter())