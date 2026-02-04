age = 17 #integer
length = 45.6 #float
greating = "hello there" #string
hasFeathers = True #boolean



#data structures-multiple values stored in one variable

fruits = ["Banana","Apple","Mango"] #list-ordered and changeable -diff datatypes
courses = ["MIT", "Data science" ,"Cyber security"] #Array-similsr datatypes
cars = ("Merceedez","Ford","Nissan","G-Wagon") #Tuple-ordered and unchangeable
Countries = {"Ethopia,Zambia,Canada"} #set-unordered and unchangeable
Student = {
    "firstname" : "Esther",
    "Course" : "MIT",
    "Age" : 19,
    "Nationality" : "Kenya",
    "Gender" : "Female"    
} #dictionary-Key value pair


print(age)
print("THE Length is" ,length)
print(fruits)
print(courses)
print(Countries)
print(Student)
print(Student["firstname"])


#Typecasting - process of converting one data type to another

print(float(age))
print(int(length))
