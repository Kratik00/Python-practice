class currencyConvertor:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def get_currency(self):
        return self.name

    def set_currency(self, curr):
        self.name = curr

    def get_rate(self):
        return self.rate

    def set_rate(self, rate_amount):
        self.rate = rate_amount


    def convert(self, amount):
        return self.rate * amount

c = currencyConvertor("USD", 20)
print(c.get_currency(), c.get_rate())
c.set_currency("RUPIYA")
c.set_rate(70)
print(f"The total amount is {c.convert(100)}")