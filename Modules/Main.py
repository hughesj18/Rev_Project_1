import Connector
import Product
import Customer
import Cart
import json





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
        customer = Customer.Customer(result[1], result[2], result[3])  #Customer class takes three arguments:  name, password, email
        return customer
    else:
        return None


username = input("Enter your username: ")
password = input("Enter your password: ")

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



print("Welcome to Nwets Bizzare Bazaar!")
print("What would you like to do?")
print("1. View products")
print("2. Add product to cart")
print("3. View cart")
# print("4. Checkout")
# print("5. View orders")
print("6. Exit")

products = Product.Product("product", "price", "category")



cart = Cart.Cart(user)

while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        products.get_all_products()
    if choice == "2":
        product_id = int(input("Enter the product ID: "))
        quantity = int(input("Enter the quantity: "))
        p = products.get_product_by_id(product_id)
        cart.add_item(p, quantity)
    if choice == "3":
        print("View cart")
        for item in cart.items:
            print(item)

    if choice == "4":
        print("Checkout")
        subtotal = cart.subtotal()
        print(f"Subtotal: {subtotal}")



    if choice == "6":
        break

        
