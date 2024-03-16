#atm system and perform its 
#1 task-displaying the remaining amount in the atm
#2-authentication of user if the user is authenticated then give him the following options 
#1-checK balance,cash withdrawl-after remaining balance,cash deposit,
#3 mini statement of the last three transactions
# card renewnal,prov
# limit for different cards rupay card-2000,visa-5000,mastercard-8000
class UserAu:
    
    def login():
        while True:
            user = input("Enter the username: ")
            pwd = input("Enter the password: ")
            if user == pwd:
                print("Login successful")
                break
            else:
                print("Login unsuccessful")
    login()