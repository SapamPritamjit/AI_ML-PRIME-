# Given a list of words:
# words =["apple","banana","kiwi","cherry","mango"]
# Create a dictionary that maps each word to its length

words =["apple","banana","kiwi","cherry","mango"]

dict = {}

for word in words:
    num = 0
    for i in word:
        num +=1
    
    dict[word] = num

print(dict)