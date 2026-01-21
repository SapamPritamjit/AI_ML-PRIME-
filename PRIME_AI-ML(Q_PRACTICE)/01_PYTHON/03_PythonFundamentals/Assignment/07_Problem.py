# Write a program that takes a string from the user and prints the number of spaces in
# the string

user_input = input("Enter any sentence: ")

count = 0

for word in user_input:
    if word == " ":
        count+=1
print(count)