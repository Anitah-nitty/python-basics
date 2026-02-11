
#parent class/super class/base class
class Animal:
    isMammal = True
    
    def speak(self):
        print("animal is speaking")
  
  #child class/sub class/derived class      
class Cat(Animal):   
    def meow(self):
        print("cat is meowing")     
    
    def climb(self):
        print("cat is climbing a tree")    
        
class donkey:
    hastail = True
    
    def move(self):
        print("donkey is moving")    
        
a = Animal()            

c = Cat()

d = donkey()






