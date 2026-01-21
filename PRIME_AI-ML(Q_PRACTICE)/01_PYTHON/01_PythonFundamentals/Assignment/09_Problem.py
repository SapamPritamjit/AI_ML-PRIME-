# Ask the user for : Principal(P), Rate(R), Time(T). Convert all to float and computes simple interest:
#  SI = (P * R * T) / 100

principal = int(input("Enter amount (invest or borrow): "))
rate = int(input("Enter rate(1-10): "))
Time = int(input("Enter time in year: "))

principal = float(principal)
rate = float(rate)
Time = float(Time)

print(f"The SI for given principal : {principal}, rate : {rate}, time : {Time} is {(principal * rate * Time) / 100}")