# Write a function is_prime(n) that returns True if n is a prime number and False 
# otherwise , using a loop

def is_prime(n):
    if(n < 2):
        return "Please enter number greater than or equal to 2."
    for i in range(2, n):
        if(n % i != 0):
            return True
        else:
            return False
    
num = int(input("Enter any number: "))

print(is_prime(num))