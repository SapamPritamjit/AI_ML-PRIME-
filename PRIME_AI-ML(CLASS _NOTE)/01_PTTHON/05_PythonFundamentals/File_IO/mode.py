# read mode
f = open("sample.txt", "r") # file object
data = f.read()
print(data)
f.close()

# write mode
f = open("sample.txt", "w") # file object
data = f.write("My name is Sapam Pritamjit\nNow i m learning python from apna collage")
f.close()

# Write append at end
f = open("sample.txt", "a") # file object
data = f.write("\nAnd it a great help to me")
f.close()

# binary mode
f = open("sample.txt", "rb") # file object
data = f.read()
print(data)
f.close()