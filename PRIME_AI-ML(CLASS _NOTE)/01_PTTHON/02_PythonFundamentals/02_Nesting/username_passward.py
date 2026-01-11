username = "admin"
passward = "pass"


username_ent = input("Please enter your username: ")
passward_wnt = input("Please enter your passward: ")

if(username_ent == username):
    if(passward_wnt == passward):
        print("Login successfully.")
    else:
        print("You enter the wrong passward.")
else:
    print("You enter the wrong username")