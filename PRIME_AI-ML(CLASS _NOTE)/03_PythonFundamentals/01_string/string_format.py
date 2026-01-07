a = 4
b = 34

sum = a + b

# normal formatting
print("The sum is {}".format(sum))
print("The language is {}".format("python"))

# index base formatting
print("The sum of {1} and {0} is {2}".format(a, b, sum))

# value base formatting
print("Values of vars {x} & {y}".format(x = 5, y = 8))


# F-string

print(f"The sum of {a} and {b} is {sum}")