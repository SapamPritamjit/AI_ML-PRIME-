word = "artificial intelligence"

target = input("Enter any word: ")
count = 0

for character in word:
    if (character == target):
        count+=1
    
print(f"The targeet found {count} time")