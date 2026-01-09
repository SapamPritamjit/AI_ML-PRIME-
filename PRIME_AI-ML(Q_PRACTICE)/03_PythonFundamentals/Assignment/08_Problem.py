# Write a program to check whether two lists share no common elements

lst1 = []
lst2 = []

n = int(input("Enter size of list: "))

for i in range(1, 3):
    for j in range(n):
        if( i == 1):
            val = input(f"Enter value for list 1 index {j}: ")
            lst1.append(val)
        elif(i == 2):
            val = input(f"Enter value for list 2 index {j}: ")
            lst2.append(val)

comb = set(lst1+lst2)

count = 0

for val in comb:
    count+=1

if count == 2 * n:
    print("There is no common element")
else:
    print("There is common element")

