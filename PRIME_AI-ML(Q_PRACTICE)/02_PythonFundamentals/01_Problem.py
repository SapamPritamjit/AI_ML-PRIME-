# Write a program that takes salary as input. Using conditional statements,calculate the final tax rate based on these rules:
# •If salary < 30, 000→5%
# •If salary is 30,000 – 70,000 → 15%
# •If salary > 70,000 → 25%



# Slab-based tax

salary = int(input("Enter your salary: "))

print("Slab-base tax....")

if(salary < 30000):
    final_tax = (salary * 5) / 100

elif(salary > 30000 and salary < 70000):
    final_tax = (30000 * 0.05) + ((salary - 30000) * 0.15)

else:
    final_tax = (30000 * 0.05) + (70000 * 0.15) + ((salary - 70000) * 0.25)

print("Final tax:", final_tax)

# Rate-based tax

print("Rate-based tax.....")

if salary < 30000:
    final_tax = salary * 0.05

elif salary <= 70000:
    final_tax = salary * 0.15

else:
    final_tax = salary * 0.25

print("Final tax:", final_tax)
