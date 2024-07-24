import Product
class Cart:
    def __init__(self, user):
        self.items = []
        self.user = user
        
    def add_item(self, item, quantity):
        self.items.append((item.name, item.price, quantity))
        print("Item added to cart")

    def __iter__(self):
        return iter(self.items)
    
    def subtotal(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        return total