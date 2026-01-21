# The user enter sastring containing a number(e.g.,"45").Convert it to:
# an integer
# a float
# a string again
# Print all three values with their types

num_str = input("Enter any number: ")

num_str = int(num_str)
print(type(num_str))
print(num_str)

num_str = float(num_str)
print(type(num_str))
print(num_str)


num_str = str(num_str)
print(type(num_str))
print(num_str)