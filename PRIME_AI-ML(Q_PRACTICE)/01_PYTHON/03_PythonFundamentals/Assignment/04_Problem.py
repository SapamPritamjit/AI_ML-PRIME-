# Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers

tup = (11, 21, 35, 44, 58, 65, 79, 80, 92)

even_tup = []
odd_tup = []

for num in tup:
    if num % 2 == 0:
        even_tup.append(num)
    else:
        odd_tup.append(num)

print(tuple(even_tup))
print(tuple(odd_tup))