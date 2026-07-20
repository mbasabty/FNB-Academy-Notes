# calculator.py

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Display results
print("\n" + "=" * 35)
print(f"{'Operation':<20}{'Result':>15}")
print("=" * 35)

print(f"{'Addition (+)':<20}{addition:>15}")
print(f"{'Subtraction (-)':<20}{subtraction:>15}")
print(f"{'Multiplication (*)':<20}{multiplication:>15}")

# Handle division by zero
if num2 == 0:
    print(f"{'Division (/)':<20}{'Error: Cannot divide by 0':>15}")
    print(f"{'Floor Division (//)':<20}{'Error: Cannot divide by 0':>15}")
    print(f"{'Modulus (%)':<20}{'Error: Cannot divide by 0':>15}")
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"{'Division (/)':<20}{division:>15}")
    print(f"{'Floor Division (//)':<20}{floor_division:>15}")
    print(f"{'Modulus (%)':<20}{modulus:>15}")

print("=" * 35)