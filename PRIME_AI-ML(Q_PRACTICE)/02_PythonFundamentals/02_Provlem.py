# Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

first_number = int(input("Enter first number: "))

second_number = int(input("Enter secong number: "))

for i in range(first_number, second_number + 1):
    if i % 2 == 0:
        print(i, end=" ")