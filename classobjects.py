
#A class is a blue print
class Employee:
   #attributes/variables 
    name = "James"
    age = 45
    gender = "male"
    salary = 70000.00
    
    #behavior/function
    
    def eat(self):
        print("Employee eats")
        
#object is an instance of a class
employee1 = Employee() #creating an object
print(employee1.name)
employee2 = Employee()        
employee3 = Employee()