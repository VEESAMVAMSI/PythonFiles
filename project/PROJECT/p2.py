import csv

class LandR:
    def register(self):
        print(""" \    _    __  __    _     ________  _   _   __  __  ___  ____  
   / \  |  \/  |  / \   |__  / _ \| \ | | |  \/  |/ _ \|  _ \ 
  / _ \ | |\/| | / _ \    / / | | |  \| | | |\/| | | | | | | |
 / ___ \| |  | |/ ___ \  / /| |_| | |\  | | |  | | |_| | |_| |
/_/   \_\_|  |_/_/   \_\/____\___/|_| \_| |_|  |_|\___/|____/ 
        """)
        print("!!!!WELCOME TO THE AMAZON STORE!!!!!")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        phoneno = input("Enter phone number: ")
        pincode = input("Enter pin code: ")    
        city = input("Enter city: ")
        

        with open('Amazon.csv', 'a', newline="") as file:
            takein = csv.writer(file)
            takein.writerow([self.username,self.password,phoneno,pincode,city])
            print("Registration successful.")

    def login(self):
        while True:
            username = input("Enter the username:")
            pwd = input("Enter the password:")
            if username == self.username and pwd == self.password:
                print("Login successful")
                break
            else:
                print("Please enter valid credentials")
obj=LandR()
obj.register()
obj.login()



