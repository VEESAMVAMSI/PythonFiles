#
class Faculty:
    def __init__(self,name,dept,id,n):
        self.name=name
        self.dept=dept 
        self.id=id
        self.n=n
        
    def attendce(self):
        pass
    def present(self,z):
        self.n=z
    def print_info(self):
        print("factulty-info",self.name,self.dept,self.id,self.n,self.z)
obj=Faculty("satya","computer science",1059,85)
obj.print_info()
obj.attendce()
obj.present(5)

