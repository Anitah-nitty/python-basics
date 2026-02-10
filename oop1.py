
class dog:
    
    
    def __init__(self,name,breed,hasfur):
        self.name = name
        self.breed = breed
        self.hasfur = hasfur
        
    def bark(self):
        print(self.name,"Woof!! Woof!!" )   
        
    def locomotive(self):
        print("Dog is walking")     
        
        
dog1 = dog("Jj","BUlldog",True)  
print(dog1.name,dog1.breed,"has fur:",dog1.hasfur) 
dog1.bark()


dog2 = dog("Tony","German Shepherd",True)  
print(dog2.name,dog2.breed,"has fur:",dog2.hasfur)   

dog3 = dog("Charles","Siberian Husky",True) 