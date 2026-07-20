# South African Fuel Cost Calculator

# Ask the user for input
kilometers = float(input("How many kilometers do you want to drive? "))
petrol_price = float(input("Enter the current petrol price per liter (R): "))

# Calculate liters needed
liters_needed = kilometers / 10

# Calculate total fuel cost
total_cost = liters_needed * petrol_price

# Display the result rounded to 2 decimal places
print("\n--- Fuel Cost Summary ---")
print("Kilometers to drive:", kilometers)
print("Liters of fuel needed:", liters_needed)
print("Total fuel cost: R", round(total_cost, 2))
