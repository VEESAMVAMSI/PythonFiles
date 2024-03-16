
def login():
    while(True):
        user=input("enter the username:")
        pwd=input("enter the password:")
        if(user==pwd):
            print("login succesful")
            break
        else:
            print("unsuccesful")
login()