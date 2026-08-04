import math as m

class polygon:
    def __init__(self, number_of_sides, *sides):
        self.number_of_sides = number_of_sides
        self.sides = sides
class triangle(polygon):
    def __init__(self, number_of_sides, *sides):
        polygon.__init__(self, number_of_sides, *sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return m.sqrt(s*(s-a)*(s-b)*(s-c))

t = triangle(3, 10, 15, 20)
print(t.area())