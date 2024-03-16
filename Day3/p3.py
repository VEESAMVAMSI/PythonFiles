#write a fun to calculate sum of first and last digit of a num
# def add(num):
    
#     first=num%10
#     last=0
#     while(num>0):
#         rem=num%10
#         num//=10
#         last=rem
#     print(first+last)      
# add(45678)       
#  
def sande(n):
    l=n%10
    while n>10:
       
       n//=10
    f=n%10
    print(f+l)
sande(22222222)
#login function with username and password -if same success else again ask user ans pwd until both are same
   
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