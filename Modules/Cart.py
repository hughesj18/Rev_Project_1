import Product
import Connector
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
    
    #Method to add a new order to the orders SQL table
    def add_order(self):
        conn = Connector.get_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO orders (customer_id, total) VALUES (%s, %s)"
        cursor.execute(query, (self.user.user['id'], self.subtotal()))
        
        conn.commit()
        conn.close()
        print("Order added successfully")