class Placements:
        def print_info(self,num):
         
         print("the number of placements",num)
         print("stilll counting")

class dept(Placements):
    def department(self):
        print("the departments are :")
        print("cse-ds")
        print("ai")
        print("civil")
        print("cse")
        print("ai&ml")
        print("mech")
        print("eee")
        print("ai")
class pragati(dept,Placements):
    def welcome(self):
        print("welcome to the college")
obj=pragati()
obj.welcome()
obj.print_info(1200)
obj.department()
