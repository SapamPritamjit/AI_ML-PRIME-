# Letʼs create a “Number Guessing Game”.Given a secret number(already decided by
# you), write a program that asks the user to guess it and prints
# "Too High" --> if the guess is above the number
# "Too Low" --> if the guess is below
# "Correct!" --> if the guess matches

import random

number = random.randint(1, 100)
# print(number)

def Number_Guessing_Game(n):
    if n > number:
        return "Too High"
    elif n < number:
        return "Too Low"
    else:
        return "Correct!"
    
user_input = int(input("Enter any number between 1 to 100: "))

print(Number_Guessing_Game(user_input))