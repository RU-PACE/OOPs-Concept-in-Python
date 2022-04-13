# Inheritance : To pass on means something which belongs to our parents then it belongs to us also.
# The below example is of single level inheritance.
class R :
    def feature1 (self):
        print("feature 1 working")
    def feature2 (self):
        print("feature 2 working")    
class U(R) :
    def feature3 (self):
        print("feature 3 working")
    def feature4 (self):
        print("feature 4 working")    
r=R()
r.feature1()
r.feature2()

u=U()
u.feature1()
u.feature2()
u.feature3()
u.feature4()