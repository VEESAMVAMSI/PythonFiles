from module1 import UserAu

class ATM:
    
    def login():
        while True:
            user = input("Enter the username: ")
            pwd = input("Enter the password: ")
            if user == pwd:
                print("Login successful")
                break
            else:
                print("Login unsuccessful")
    def rupay(self,amount):
        self.amount=amount
        if amount<2000:
            print("enter the amount")
        else:
            print("limit exceed")
    rupay()
    def visa(self,amount):
        self.amount=amount
        if amount<2000:
            print("enter the amount")
        else:
            print("limit exceed")
    visa()
    def mastercard(self,amount):
        self.amount=amount
        if amount<2000:
            print("enter the amount")
        else:
            print("limit exceed")
    mastercard()