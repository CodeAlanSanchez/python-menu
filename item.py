
class Item():

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
