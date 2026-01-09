# Write a function to return the sum of digits of a number, n

n = int(input("Enter any number: "))

sum = 0

while n != 0:
    las = n % 10
    n //=10
    sum +=las

print(sum)