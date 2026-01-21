# Write a function that prints the digits of a number, n.
# For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them


num = int(input("Enter any number: "))

lst = []

while num != 0:
    val = num % 10
    lst.append(val)
    num //=10

lst.reverse()
print("All digits of a given number is : ",lst)