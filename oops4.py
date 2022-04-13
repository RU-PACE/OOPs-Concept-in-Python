                                                        # Types of variables:
# 1) Instance variable:
# These variables are different for different objects. If we change one object, it will not affect other objects.These are defined under "init" function.
# Example
class Car:
    def __init__(self):
        self.mil = 10
        self.com = "Mahindra"
c1=Car()
c2=Car()
c1.mil=8
print(c1.com, c1.mil)
print(c2.com, c2.mil)

# 2) Class variable: A variable,  when it is changed it will affect all other objects.These are defined outside "init" function.
class Car:
    wheels =4
    def __init__(self):
        self.mil = 10
        self.com = "Mahindra"
c1=Car()
c2=Car()
c1.mil=8
Car.wheels=5 # This change affects all the value of objects.
print(c1.com, c1.mil,c1.wheels)
print(c2.com, c2.mil,c2.wheels)

