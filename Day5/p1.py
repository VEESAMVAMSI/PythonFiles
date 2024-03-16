# create a class of name "placements "which has a finction info which displays "the number of placements"
#create another class dept  with funtion display which will display names of the departments present in the college
# create a class pragati with function welcome ,which displays the msg we are glab have u on board
#pragati class should also display the details about depts and placements ,


class Placements:
        def print_info(self,num):
         
         print("the number of placements",num)

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
class pragati(dept):
    def welcome(self):
        print("welcome to the college")
obj=pragati()
obj.welcome()
obj.print_info(1200)
obj.department()

