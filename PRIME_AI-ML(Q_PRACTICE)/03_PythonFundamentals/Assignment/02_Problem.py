# Given a list of integers compute the average of all numbers in the list

# lst = [12, 34, 56, 78]

n = int(input("Enter the size of list: " ))

lst = []
for i in range(n):
    a = int(input("Enter number: "))
    lst.append(a)

sum = 0

for num in lst:
    sum+=num

print("The average of a given list is: ", sum / n)