class Father():
    def bike(self):
        print("glamour")
    def laptop(self):
        print('1tb')
class pavan(Father):
    def laptop(self):
        print("10tb")
    def bike(self):
        print("jawa")
obj=pavan()
obj.bike()
obj.laptop()