# Input two lists of integers from the user. Merge them into one list and sort 
# the result

lst1 = []
lst2 = []

n = int(input("Enter the size of list: "))

for i in range(1, 3):
    for j in range(n):
        val = int(input(f"Enter the value for {i} list: "))
        if i == 1:
            lst1.append(val)
        else:
            lst2.append(val)

merge = list(set(lst1 + lst2))
merge.sort()
print(merge)