def welcome_message(company_name):
    if company_name.lower() == "mercedes":
        return "Welcome to Mercedes-Benz!"
    elif company_name.lower() == "mahindra":
        return "Welcome to Mahindra!"
    elif company_name.lower() == "toyota":
        return "Welcome to Toyota!"
    else:
        return "Welcome! Please specify a valid car company."

def variant(company_name, model_name):
    if company_name.lower() == "mercedes":
        if model_name.lower() == "c-class":
            return "Variant: Petrol"
        elif model_name.lower() == "e-class":
            return "Variant: Diesel"
    elif company_name.lower() == "mahindra":
        if model_name.lower() == "xuv500":
            return "Variant: Petrol"
        elif model_name.lower() == "scorpio":
            return "Variant: Diesel"
    elif company_name.lower() == "toyota":
        if model_name.lower() == "corolla":
            return "Variant: Petrol"
        elif model_name.lower() == "innova":
            return "Variant: Diesel"
    return "Invalid company or model name."

def calculate_price(ex_showroom_price):
    cgst = 0.06 * ex_showroom_price
    sgst = 0.06 * ex_showroom_price
    insurance = 0.03 * ex_showroom_price
    on_road_price = ex_showroom_price + cgst + sgst + insurance
    return on_road_price

company_name = input("Enter the car company name (Mercedes, Mahindra, Toyota): ")
print(welcome_message(company_name))

if company_name.lower() in ["mercedes", "mahindra", "toyota"]:
    model_name = input("Enter the specific model name: ")

    if company_name.lower() == "mercedes":
        if model_name.lower() == "c-class":
            ex_showroom_price = 4000000
        elif model_name.lower() == "e-class":
            ex_showroom_price = 4500000
    elif company_name.lower() == "mahindra":
        if model_name.lower() == "xuv500":
            ex_showroom_price = 1500000
        elif model_name.lower() == "scorpio":
            ex_showroom_price = 1400000
    elif company_name.lower() == "toyota":
        if model_name.lower() == "corolla":
            ex_showroom_price = 1800000
        elif model_name.lower() == "innova":
            ex_showroom_price = 2000000

    if model_name.lower() in ["c-class", "e-class", "xuv500", "scorpio", "corolla", "innova"]:
        print("Ex-showroom price: ₹", ex_showroom_price)
        on_road_price = calculate_price(ex_showroom_price)
        print("On-road price: ₹", on_road_price)
    else:
        print("Invalid model name.")
