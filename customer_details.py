class customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_phone(self):
        return self.phone_number

    def set_phone(self, number):
        self.phone_number = number

num = customer("Roshni", 1122334455)
print(num.get_phone())
num.set_phone(9988776655)
print(num.get_phone())