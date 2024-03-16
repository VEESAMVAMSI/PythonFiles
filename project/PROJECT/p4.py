from p2 import LandR
from p3 import ProductManager, Product

def main():
    
    user_manager = LandR()
    product_manager = ProductManager()
    user_manager.register()
    user_manager.login()
    product_manager.show_available_products()
    selection = input("Enter the index or name of the product you want to purchase: ")
    quantity = int(input("Enter the quantity you want to purchase: "))
    total_cost = product_manager.purchase_product(selection, quantity)
    print(f"Your total cost is: {total_cost}")

   
    print("Thank you for purchasing! Please visit again.")
    print("Please give us a review.")


