import Connector
import json

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.price} - {self.category}"
        

    @staticmethod
    def get_all_products():
        conn = conn = Connector.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM products"
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            name = row[1]
            price = row[2]
            category = row[3]

            print(f"{name} - {price} - {category}")
        
        conn.close()
    
    def get_product_by_id(self, id):
        conn = Connector.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM products WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        if result:
            self.name = result[1]
            self.price = result[2]
            self.category = result[3]
            #print name, price, category to console
            print(f"{self.name} - {self.price} - {self.category}")
            return self
        else:
            return False

    
    def create_table(self):
        conn = Connector.get_connection()
        cursor = conn.cursor()


        query = "DROP TABLE IF EXISTS products"
        cursor.execute(query)
        query = "CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price FLOAT, category VARCHAR(255))"
        cursor.execute(query)

        conn.commit()
        conn.close()
        print("Table created successfully")

    def load_products(self):
        conn = conn = Connector.get_connection()
        cursor = conn.cursor()

        with open('products.json') as file:
            products_data = json.load(file)


        for product in products_data['products']:
            name = product['name']
            category = product['category']
            price = product['price']

        
            query = "INSERT INTO products (name, category, price) VALUES (%s, %s, %s)"
            values = (name, category, price)
            cursor.execute(query, values)
        
        conn.commit()
        conn.close()  
        print("Products loaded successfully")  
