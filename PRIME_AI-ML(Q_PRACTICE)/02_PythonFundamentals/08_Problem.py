# Letʼs create a Simple Calculator that performs arithmetic operations. Create 
# a function "calculator(a, b, operator)" that performs addition, subtraction, 
# multiplication, or division based on the parameter

def calculator(a, b, operator):
     if operator == "+" or "1":
          return a + b
     elif operator == "-" or "2":
          return a - b
     elif operator == "*" or "2":
          return a * b
     elif operator == "/" or "4":
          return a / b
     elif(operator.lower() == "exit" or "5"):
          return "Exiting...."


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Please select any operation:\n1) Addition (+)\n2) Subtraction (-)\n3) Multiplication (*)\n4) Division (/)\n5) Exit.")

operator = input("Please enter according to the given option: ")
print(calculator(a, b, operator))