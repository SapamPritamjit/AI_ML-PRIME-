# Ask the user to enter two integers and one float.Convert them all to floats and print their average

num1 = int(input("Enter integer value: "))

num2 = int(input("Enter integer value: "))

num3 = float(input("Enter floating value: "))

num1 = float(num1)
num2 = float(num2)

print(f"The average for {num1}, {num2} and {num3} is {(num1 + num2 + num3)/3}")