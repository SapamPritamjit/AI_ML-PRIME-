# Create a dictionary where
# Keys = student names
# Values = marks(integer)
# Write a menu - based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) depending on
# the operation they want to perform on the dictionary:
# A - Add a student
# B - Update marks
# C - Search for a student
# D - Display all students and marks

dict = {
    "Rohit" : 67,
    "Ram" : 78,
    "Thoibi" : 56
}

def student_info(choice):
    if choice == "A":
        name = input("Enter student name: ")
        dict.update({name : None})
        return "Adding successfully.."
    elif choice == "B":
        name = input("Enter student name: ")
        if name not in dict:
            return "Name not found"
            
        mark = int(input("Enter mark: "))
        dict[name] = mark
        return "update successfully.."

    elif choice == "C":
        name = input("Please enter student name: ")
        return dict.get(name)
    
    elif choice == "D":
        return dict.items()
while True: 
    print("Menu....")
    print("A - Add a student\nB - Update marks\nC - Search for a student\nD - Display all students and marks\nE - Exit")
    choice = input("Enter your choice: ")


    if choice == "E" or choice == "exit":
        print("Exiting...")
        break
    else:
        print(student_info(choice))

