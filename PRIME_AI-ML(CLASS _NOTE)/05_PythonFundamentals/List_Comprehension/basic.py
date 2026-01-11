# Normal way
numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)

# With list comprehension
numbers1 = []
numbers1 = [i for i in range(5)]
print(numbers1)

# With condition
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)


lst = [-5, 5, 7, 9, -2, 6]
res = [0 if val < 0 else val for val in lst]
print(res)