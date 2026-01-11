f = open("sample.txt", "r") # file object

# data = f.read()
# print(data)

data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()