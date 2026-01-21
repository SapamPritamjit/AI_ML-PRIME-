# Design a program to continuously input a number from user & print if it is 
# positive or negative until the user enters “Quit”

while True:
    user_input = input("Enter any number or (quit to exit): ")
    if(user_input.lower() != "quit"):
        user_input = int(user_input)
        if(user_input > 0):
            print("Positive")
        elif(user_input < 0):
            print("Negative")
        else:
            print("Its zero")
    elif(user_input.lower() == "quit"):
        print("Exiting...")
        break