# alternative for if elif else

user = input("Enter color('red', 'yellow', 'green'): ")

match user:
    case "red":
        print("Go")
    case "yellow":
        print("Ready")
    case "green":
        print("Go")
    case _:
        print("Wrong color")