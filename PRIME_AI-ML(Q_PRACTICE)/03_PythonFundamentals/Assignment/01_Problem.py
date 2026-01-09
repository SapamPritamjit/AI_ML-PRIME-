# Ask the user for a string and check whether it is a palindrome or not.
# A palimdrome is a string which is same when we read it forward & backward. 
# Eg-“madam”,“racecar”etc

word = input("Enter a any word: ")

rev_word = word[::-1]

if rev_word == word:
    print("Palimdrome")
else:
    print("Not Palimdrome")


# rev_word = ""
# for chr in word:
#     rev_word = chr + rev_word

# if rev_word == word:
#     print("Palimdrome")
# else:
#     print("Not Palimdrome")
