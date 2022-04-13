                                                                  # Constructor & Self
#  1) Constructor 
class Computer:
    pass      # It keeps the class empty.
c1=Computer() # This bracket is a constructor.
c2=Computer()
print(id(c1))
print(id(c2))
# Every time we create an object it is allocated into a new space called as heap memory.
# Size of object depends on the no of variables and size of each variables.
# And its allocation to a perticular memory location is done by  "Constructor".



#  2) "Self" refers to a object and it plays very important role. for example
class Computer:

   def __init__(self): 
    self.name="Rupesh"
    self.age= 20

   def update(self):
       self.name="shivam"

c1=Computer()
c2=Computer()

#print(c1.name)
#print(c2.name)

c1.update() # After this instruction the pointer moves to def update "line no 19". So, how it will know that for which object we are talking about.
# Here comes the use of self. It will point the object based on our calling object and in bracket it will pass "c1".


print(c1.name)
print(c2.name)

