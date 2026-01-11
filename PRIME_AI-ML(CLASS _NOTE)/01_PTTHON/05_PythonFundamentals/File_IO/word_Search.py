# with open("sample.txt", "r") as f:
#     data = f.read()

#     if("python" in data):
#         print("It exist")
#     else:
#         print("The word is not exist")


line = 0

with open("sample.txt", "r") as f:
    while True:
        line+=1
        data = f.readline()
        if("python" in data):
            print(f"Word found in {line} line")
            break
        