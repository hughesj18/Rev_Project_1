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
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            name = row[1]
            price = row[2]
            category = row[3]

            product = Product(name, price, category)
            print(product)
    

def load_products():
    conn = conn = Connector.get_connection()
    cursor = conn.cursor()

        #run a query to drop the table if it exists
    query = "DROP TABLE IF EXISTS products"
    cursor.execute(query)
    query = "CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price FLOAT, category VARCHAR(255))"
    cursor.execute(query)

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
load_products()