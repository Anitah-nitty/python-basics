number = int(input("Enter first Number :"))
operator = input("enter operator (+ , - , * , /)")
num = int(input("Enter second Number :"))

if operator== "+":
    print("Answer :",number + num)
    
elif operator == "-":
    print("Answer :",number - num)    
    
elif operator == "*":
    print("Answer :",number * num)    
    
elif operator == "/":
    if num != 0 :
     print("Answer :",number / num)  
    else :
        print("invalid answer")   
    
else :
    print("invalid operator")           