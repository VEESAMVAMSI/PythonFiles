# create a class with f15 with lights and fans and when lights is called it prints out color of the light which is  
# is taken as parameter to the funtion,when fan function is called it displays the
# speed regulator
# ac-displays the room temperqture and the outside  tempurature  
# write a forth funtion -whose name is displays the diiference in outside temp  and room temp and also it 
# displays fan speed
#constructor is a funtion it runs as soon as an obj is created and memory allocates


class f15:
    def __init__(vamsi,y,z):
        vamsi.y=y
        vamsi.z=z
        print("palcements-1200")

    def light(vamsi,a):
        print('The color of the light:',a)
    def fan(vamsi,b):
        vamsi.b=b
        print('The speed of the fan is:',b)
    def ac(vamsi,c,d,):
        print('The temp outside:',c)
        print('The temp inside:',d)
        vamsi.c=c
        vamsi.d=d
        vamsi.e=d-c
    def display(vamsi):
        print('The diferrence is:',vamsi.e)
        print("The Fan speed:",vamsi.b)
        print("the start time",vamsi.y)
        print("the end time",vamsi.z)
obj=f15(0,8)
obj.light('Orange')
obj.fan(50)
obj.ac(34,22)
obj.display()
