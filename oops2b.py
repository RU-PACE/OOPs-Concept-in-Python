# This program is the combination of varibles and methods.
class Rupesh:

   def __init__(self,cpu,ram): 
    self.cpu=cpu
    self.ram=ram

   def config(self):
    print("Config is", self.cpu,self.ram) 

Com1=Rupesh("i5",8)
Com2=Rupesh("i3",8)

Com1.config() 
Com2.config()    