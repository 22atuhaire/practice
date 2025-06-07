operator = input("Enter an operator (+,- * /): ")

num1 = float(input("Enter on number: "))
num2 = float(input("Enter on number: "))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
    
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
    
elif operator == "*":
    result = num1*num2
    print(round(result,3))
    
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
    
else:
    print( f"The {operator} is an invalid operator")
   
  