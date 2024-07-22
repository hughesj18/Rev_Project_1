import Connector
import Product




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

print("Welcome to Nwets Bizzare Bazaar!")
print("What would you like to do?")
print("1. View products")
# print("2. Add product to cart")
# print("3. View cart")
# print("4. Checkout")
# print("5. View orders")
# print("6. Exit")

products = Product.Product("product", "price", "category")

choice = input("Enter your choice: ")
if choice == "1":
    print("Products:")
    products.get_all_products()
    
