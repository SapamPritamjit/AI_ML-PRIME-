# Ask the user for a string and print
# All unique characters
# The count of unique characters

user_input = input("Enter any word: ")

unique_char = (set(user_input))

print(unique_char)

count = 0

for word in unique_char:
    count+=1

print(count)