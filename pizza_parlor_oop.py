class pizza:

    def __init__(self):
        self.base_price = 10.00
        self.topping_price = 1.50
        self.valid_toppings =["pepperoni", "mushrooms", "extra cheese"]
        self.topping_count = 0

    def calculate_total(self, topping_count):
        total = self.base_price + (topping_count * self.topping_price)
        return total

