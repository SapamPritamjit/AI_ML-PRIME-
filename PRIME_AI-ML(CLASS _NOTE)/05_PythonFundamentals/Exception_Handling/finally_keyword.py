try:
    x = int(input("Enter any number: "))
    ans = 10/x
except ZeroDivisionError:
    print(f"division by zero is not allowed")
except ValueError:
    print(f"Invalid input")
else:
    print(f"ans = {ans}")
finally:
    print("End of program")