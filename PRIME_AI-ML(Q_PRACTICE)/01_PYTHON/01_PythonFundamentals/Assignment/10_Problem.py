# Take a decimal number as input (like 45.75) and output its:
# Integer part : 45
# factorial part : .75

# num = float(input("Plese enter number in floating type: "))

# int_num = int(num)

# print(f"Integer part : {int_num} and factorial part : {(num - int_num)}")

num = float(input("Please enter number in floating type: "))

integer_part = int(num)
fractional_part = num - integer_part


fractional_part = round(fractional_part, 2)

print(f"Integer part : {integer_part} and fractional part : .{str(fractional_part).split('.')[1]}")
