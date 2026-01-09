# Given a list, print all elements that appear more than once in the list

lst = []

n = int(input("Enter any number: "))

for i in range(n):
    num = int(input("Enter element for list: "))
    lst.append(num)

lst.sort()

commom_element = 0

for val in lst:
    if val != commom_element:
        commom_element = val
    else:
        print(commom_element)