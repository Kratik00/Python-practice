import random
class dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return random.randint(1, self.sides)

r = dice(6)
print(r.roll_dice())