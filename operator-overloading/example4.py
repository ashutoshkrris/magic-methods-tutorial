class ShoppingBasket:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


# Creating a shopping basket object
my_basket = ShoppingBasket(["Apple", "Mango", "Pineapple"])

# Checking if an item exists in the basket
result = "Apple" in my_basket
print(result)

result = "Oranges" in my_basket
print(result)
