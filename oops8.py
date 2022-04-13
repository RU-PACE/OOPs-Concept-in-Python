#Polymorphism 
# Duck Typying
class Pycharm:
    def execute(self):
        print("compling")
        print ("running")
class Myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compling")
        print ("running") 
class Laptop:
    def code(self,ide):
        ide.execute()

ide=Myeditor()

lap1=Laptop()
lap1.code(ide)             