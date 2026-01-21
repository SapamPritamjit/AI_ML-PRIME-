# Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print temperature in Fahrenheit

# Conversion formula : FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

temp = input("Enter temperature in celsius: ")

temp = float(temp)

print("Celsius to Fahrenheit conversion....")
print(f"{temp} celsius = {(temp * (9 / 5) + 32)} Fahrenheit")