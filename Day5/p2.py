#create a class Ticket which will be the abstract class inside that create funtion book ticket which will be the
#and has nothing in it .
# create a class  make my trip  which will usr the book ticket funtion from ticket class to take the details 
# such as name,ph no email.id ,journeydate ,and displays a msg thanku for booking from make my trip.
# create a class irctc which uses the book ticket of the 
# take the same details for the makemytrip ,but at the end it will give the option to select it is one way or long trip
#     if the user input is round or long trip ,it should ask the user to enter return date as well and then prints the msg
# "tq for choosing the ircts else proint the msg tq for choosing irctc ."
# #create a class indigo all the details as irctc and just asks whic mode of transport u want to go in  train ,palne ,bus  
# and diplay tq for chosing 

from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def book_tickets(self):
        pass
class makeMyTrip(Ticket):
    def book_tickets(self):
        name=input("name:")
        ph_no=int(input("ph:"))
        id=int(input("id"))
        email=input("email:")
        j_date=input("date:")
        self.name=name 
        self.ph_no=ph_no 
        self.id=id 
        self.email=email
        self.j_date=j_date  
    def display(self):
       print("thank you for using makeMyTrip")
class irctc(makeMyTrip):
    def trip_type(self):
        print("type of trip,one_way or round the trip(select 1 or 2)")
        n=int(input("num"))
        if n==1:
            print("thank u for choosing  irctc")
        elif n==2:
            print("enter your return date:")
            n=int(input("date"))
            print("your return date ",n)
            print("thank u for choosing  irctc")
class indigo(irctc):
    def mode(self):
        print("which type of transport u want Train,Bus,Plane")
        n=input("")
        print("thanks for booking indigo")
obj=indigo()
obj.book_tickets()
obj.trip_type()
obj.mode()
