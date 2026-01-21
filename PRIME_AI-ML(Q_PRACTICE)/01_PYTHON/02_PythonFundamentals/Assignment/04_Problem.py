# Write a function to return the count the number of digits in a number, n

n = int(input("Enter any number: "))

count = 0

while n != 0:
    n //=10
    count+=1

print(count)