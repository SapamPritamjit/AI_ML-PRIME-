# Write a program to swap values of two numbers entered by the user

num1 = int(input("Enter any number: "))

num2 = int(input("Enter any number: "))

print("Before swaping....")
print(f"num1 = {num1} and num2 = {num2}")

# swap
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping....")
print(f"num1 = {num1} and num2 = {num2}")