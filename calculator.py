class calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def product(a, b):
        return a * b
    @staticmethod
    def division(a, b):
        return a / b
print(calculator.add(5, 6))
print(calculator.subtract(6, 5))
print(calculator.product(9, 7))
print(calculator.division(9, 3))