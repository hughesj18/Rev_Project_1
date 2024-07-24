import json
import Connector

class Customer:
    def __init__(self, name, password, email):
        self.user = {
            'username': name,
            'pass': password,
            'email': email
        }
        #self.orders = []  --implement order history later

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def add_to_cart(self, product):
        
        self.cart.append(product)
        print(f"{product.name} added to cart")



    def load_users():
        conn = Connector.get_connection()
        cursor = conn.cursor()

        query = "DROP TABLE IF EXISTS users"
        cursor.execute(query)
        query = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), pass VARCHAR(255), email VARCHAR(255), adminCred BOOLEAN DEFAULT FALSE)"
        cursor.execute(query)

        with open('users.json') as file:
            users_data = json.load(file)

        for user in users_data['users']:
            
            username = user['name']
            password = user['password']
            email = user['email']

            query = "INSERT INTO users (username, pass, email, adminCred) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, password, email, False))
        print("Users loaded successfully")

        conn.commit()
        conn.close()
#Customer.load_users()