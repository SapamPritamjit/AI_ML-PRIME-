vowel = {"a", "e", "i", "o", "u"}

word = "artificial intelligence"
count = 0

for tar in word:
    if tar in vowel:
        count +=1

print(f"{count} number of vowel found.")