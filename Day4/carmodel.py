class CarShowroom:
    def __init__(self, company_name):
        self.company_name = company_name
        print(f"Welcome to the {self.company_name} showroom.")

    def model_name(self, model):
        pass

    def variant(self, fuel):
        pass

    def price(self, ex_showroom_price):
        cgst = 0.06 * ex_showroom_price
        sgst = 0.06 * ex_showroom_price
        insurance = 0.05 * ex_showroom_price
        onroad_price = ex_showroom_price + cgst + sgst + insurance
        print(f"Ex-showroom price: {ex_showroom_price}")
        print(f"Central CGST: {cgst}")
        print(f"State SGST: {sgst}")
        print(f"Insurance: {insurance}")
        print(f"On-road price: {onroad_price}")


def main():
    options = {"1": "mercedes", "2": "mahindra", "3": "toyota"}
    lis = ["1. MERCEDES", "2. MAHINDRA", "3. TOYOTA"]
    choice = input(f"Please select the car company (1-3):\n{'\n'.join(lis)}\n")

    company_name = options.get(choice)

    if not company_name:
        print("Invalid input. Please enter a number between 1 and 3.")
        return main()

    showroom = CarShowroom(company_name)

    model = input(f"Please enter the specific model name for {company_name}: ")

    fuel_options = {"1": "petrol", "2": "diesel"}
    fuel_lis = ["1. Petrol", "2. Diesel"]
    fuel_choice = input(f"Please select the fuel type for {company_name} (1-2):\n{'\n'.join(fuel_lis)}\n")
    fuel_type = fuel_options.get(fuel_choice)

    if not fuel_type:
        print("Invalid input. Please enter a number between 1 and 2.")
        return main()

    showroom.model_name(model)
    showroom.variant(fuel_type)
    showroom.price(5000000)  # Default ex-showroom price


if __name__ == "__main__":
    main()
