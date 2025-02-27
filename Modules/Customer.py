import json
import Connector

class Customer:
    def __init__(self, id, name, password, email, adminCred=False):
        self.user = {
            'id': id,
            'username': name,
            'pass': password,
            'email': email,
            'adminCred': adminCred
        }
        self.orders = []  # List to store the orders
        self.adminCred = adminCred 
    
    def get_admin_status(self):
        result = self.user['adminCred']
        return result

    def display_info(self):
        print(f"ID: {self.user['id']}")
        print(f"Name: {self.user['username']}")
        print(f"Admin: {bool(self.user['adminCred'])}")
        print(f"Email: {self.user['email']}")

    def add_to_cart(self, product):
        
        self.cart.append(product)
        print(f"{product.name} added to cart")

    def display_purchases(self):
        conn = Connector.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM orders WHERE customer_id = %s"
        cursor.execute(query, (self.user['id'],))

        result = cursor.fetchall()

        for order in result:
            print(f"Order ID: {order[0]}")
            print(f"Total: {order[2]}")
            print("")
            query = "SELECT * FROM orders WHERE orderNum = %s"
            cursor.execute(query, (order[0],))
            items = cursor.fetchall()
            



    # Method to drop and create the users table
    def create_table(self):
        conn = Connector.get_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS users"
        cursor.execute(query)
        query = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), pass VARCHAR(255), email VARCHAR(255), adminCred BOOLEAN DEFAULT FALSE)"
        cursor.execute(query)
        print("Table created successfully")

        conn.commit()
        conn.close()
    # Method to load the users from a .json file


    def load_users(self):
        conn = Connector.get_connection()
        cursor = conn.cursor()


        with open('users.json') as file:
            users_data = json.load(file)

        for user in users_data['users']:
            
            username = user['name']
            password = user['password']
            email = user['email']
            adminCred = user['adminCred']

            query = "INSERT INTO users (username, pass, email, adminCred) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, password, email, adminCred))
        print("Users loaded successfully")

        conn.commit()
        conn.close()
# user = Customer("admin", "admin", "admin", True)
# user.create_table()
# user.load_users()