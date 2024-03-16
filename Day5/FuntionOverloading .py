#python -polymorhphism -funtionoverloading is not possible
class Arith:
        def add(self,a):
                print(a)
        def add(self,a,b):
                print(a+b)
        def add(self,a,b,c):
                print(a+b+c)
obj=Arith()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)
                
        