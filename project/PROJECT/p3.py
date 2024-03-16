class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

class ProductManager:
    def __init__(self):
        self.products = []
        self.load_products()

    def load_products(self):
        products_data = [
            ("Earphones", 2999, "Electronics", 100),
            ("Shirts", 1999, "Apparel", 50),
            ("Watches", 9999, "Accessories", 30),
            ("Laptops", 89999, "Electronics", 20)
        ]
        
        for data in products_data:
            name, price, category, stock = data
            self.products.append(Product(name, price, category, stock))

    def show_available_products(self):
        print("Available Products:")
        for idx, product in enumerate(self.products):
            print(f"{idx + 1}. {product.name} - Price: {product.price}, Stock: {product.stock}")

    def purchase_product(self, selection, quantity):
        if selection.isdigit():  # User selected by index
            idx = int(selection)
            if 0 < idx <= len(self.products):
                product = self.products[idx - 1]
                if product.stock >= quantity:
                    total_cost = product.price * quantity
                    product.stock -= quantity
                    print(f"You purchased {quantity} {product.name}(s)")
                    print(f"Cost: {total_cost}")
                    return total_cost
                else:
                    print("Insufficient stock!")
                    return 0
            else:
                print("Invalid product selection.")
                return 0
        else:  # User selected by name
            for product in self.products:
                if product.name.lower() == selection.lower():
                    if product.stock >= quantity:
                        total_cost = product.price * quantity
                        product.stock -= quantity
                        print(f"You purchased {quantity} {product.name}(s)")
                        print(f"Cost: {total_cost}")
                        return total_cost
                    else:
                        print("Insufficient stock!")
                        return 0
            print("Invalid product selection.")
            return 0
product_manager = ProductManager()
product_manager.show_available_products()
selection = input("Enter the index or name of the product you want to purchase: ")
quantity = int(input("Enter the quantity you want to purchase: "))
total_cost = product_manager.purchase_product(selection, quantity)
print(f"Your total cost is: {total_cost}")
print("Thank you for purchasing! Please visit again.")
print("Please give us a review.")
