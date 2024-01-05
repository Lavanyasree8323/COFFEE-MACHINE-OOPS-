class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "Water": 3000,
            "Milk": 2000,
            "Coffee": 1000,
        }

    def report(self):
        """Prints a report of all resources"""
        print(f"Water: {self.resources['Water']}ml")
        print(f"Milk: {self.resources['Milk']}ml")
        print(f"Coffee: {self.resources['Coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is Your {order.name}. Enjoy!")
