import Connector
import Product
import Customer
import Cart
import json
import logging



logging.basicConfig(filename="Animal_Journal.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
def check_credentials(username, password):
    
    conn = Connector.get_connection()
    cursor = conn.cursor()


    # Execute the query to check the credentials
    query = "SELECT * FROM users WHERE username = %s AND pass = %s"
    cursor.execute(query, (username, password))

    # Fetch the result
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Return True if the credentials are valid, False otherwise
    if result:
        return True
    else:
        return False

def log_in(username, password):
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # Execute the query to check the credentials
    query = "SELECT * FROM users WHERE username = %s AND pass = %s"
    cursor.execute(query, (username, password))

    # Fetch the result
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result:
        customer = Customer.Customer(result[0], result[1], result[2], result[3], result[4])  #Customer class takes three arguments:  name, password, email
        return customer
    else:
        return None


username = input("Enter your username: ")
password = input("Enter your password: ")

logging.info(f"Attempting to load {username}...")


auth = False
while not auth:
    if check_credentials(username,password):
        print("Credentials are valid")
        auth = True
    else:
        print("Credentials are invalid")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
user = log_in(username, password)

logging.info(f"User {username} loaded successfully")

print("Welcome to the Bazaar Between Time!")
print("What would you like to do?")
print("1. View products")
print("2. Add product to cart")
print("3. View cart")
print("4. Checkout")
print("5. View account")
print("6. View orders")
if bool(user.adminCred):
    print("7. Admin: Drop and recreate table for products")
    print("8. Admin: Load products from file")
    print("9. Admin: Reload users from file") 
print("0. Exit")
products = Product.Product("product", "price", "category")



cart = Cart.Cart(user)


while True:
    choice = input("Enter your choice (help for list): ")
    if choice == "help":
        print("1. View products")
        print("2. Add product to cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. View account")
        print("6. View orders")
        if bool(user.adminCred):
            print("7. Admin: Drop and recreate table for products")
            print("8. Admin: Load products from file")
            print("9. Admin: Reload users from file") 
        print("0. Exit")
    if choice == "1":
        logging.info("Fetching all products...")
        products.get_all_products()
    if choice == "2":
        logging.info("Fetching product from products by ID...")
        product_id = int(input("Enter the product ID: "))
        quantity = int(input("Enter the quantity: "))
        p = products.get_product_by_id(product_id)
        cart.add_item(p, quantity)
    if choice == "3":
        print("View cart")
        for item in cart.items:
            print(item)
        print(f"Subtotal: {cart.subtotal()}")
    if choice == "4":
        print("Checkout")
        subtotal = cart.subtotal()
        print(f"Subtotal: {subtotal}")
        logging.info(f"Adding order to orders table for {user.user['username']}...")
        cart.add_order()
        logging.info(f"Order added successfully for {user.user['username']}")
    if choice == "5":
        print("View account")
        user.display_info()
    if choice == "6":
        print("View orders")
        print("")
        logging.info(f"Displaying purchases for {user.user['username']}...")
        user.display_purchases()
        logging.info(f"Purchases displayed successfully for {user.user['username']}") 

    # Admin options    
    if choice == "7" and bool(user.adminCred):
        logging.info("Dropping and recreating products table...")
        products.create_table()
        logging.info("Table dropped and recreated successfully")
    if choice == "8" and bool(user.adminCred):
        logging.info("Loading products from file...")
        products.load_products()
        logging.info("Products loaded successfully")
    if choice == "9" and bool(user.adminCred):
        logging.info("Recreateing users table...")
        user.create_table()
        logging.info("Users table recreated successfully")
        logging.info("Loading users from file...")
        user.load_users()
        logging.info("Users loaded successfully")
    if choice == "0":
        break